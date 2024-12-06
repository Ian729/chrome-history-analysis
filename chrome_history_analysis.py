import os
import shutil
import sqlite3
import pandas as pd
from urllib.parse import urlparse

def copy_chrome_history(src_path, dest_path):
    """
    Copies the Chrome history file to avoid database lock errors.
    """
    try:
        shutil.copy2(src_path, dest_path)
        print(f"Copied History file to {dest_path}")
    except FileNotFoundError:
        print(f"Source file not found at {src_path}. Please verify the path.")
        exit()

def extract_data(history_db_path):
    """
    Extracts browsing history data from the copied Chrome History database.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(history_db_path)
    cursor = conn.cursor()

    # Query the URLs table
    query = """
    SELECT url, title, visit_count, last_visit_time
    FROM urls
    ORDER BY visit_count DESC
    LIMIT 10;
    """
    cursor.execute(query)

    # Fetch results
    results = cursor.fetchall()
    conn.close()

    return results

def analyze_domains(history_data):
    """
    Analyzes the most visited domains from the browsing history.
    """
    domain_counts = {}
    for row in history_data:
        url = row[0]
        domain = urlparse(url).netloc
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

    # Convert to a sorted DataFrame for analysis
    df = pd.DataFrame(domain_counts.items(), columns=["Domain", "Visit Count"])
    df = df.sort_values("Visit Count", ascending=False)
    return df

def main():
    # Define paths
    original_history_path = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/History")  # Adjust for your OS
    copied_history_path = "History_copy"

    # Step 1: Copy the History file
    copy_chrome_history(original_history_path, copied_history_path)

    # Step 2: Extract data
    history_data = extract_data(copied_history_path)
    if not history_data:
        print("No data found in the History database.")
        return

    # Step 3: Analyze domains
    print("\nTop 10 Visited URLs:")
    for row in history_data:
        print(f"URL: {row[0]}, Title: {row[1]}, Visit Count: {row[2]}")

    domain_df = analyze_domains(history_data)
    print("\nMost Visited Domains:")
    print(domain_df)

    # Optional: Export results
    domain_df.to_csv("most_visited_domains.csv", index=False)
    print("\nResults saved to most_visited_domains.csv")

if __name__ == "__main__":
    main()