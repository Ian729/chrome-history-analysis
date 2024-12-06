# Chrome History Analysis

This project provides a Python script to analyze Chrome browsing history. It extracts data from Chrome's SQLite database, identifies the most visited URLs and domains, and exports the results to a CSV file for further analysis.

## Features
- Automatically copies Chrome's `History` file to avoid database lock errors.
- Retrieves the top 10 most visited URLs with their titles and visit counts.
- Aggregates visit data by domain for analysis.
- Exports the results to a CSV file (`most_visited_domains.csv`).

## Prerequisites
- Python 3.7 or later
- `pandas` library

Install dependencies:
```
pip install pandas
```

## How to Use
1.	Locate Chrome’s History File:
- Windows: C:\Users\<Username>\AppData\Local\Google\Chrome\User Data\Default\History
- macOS: ~/Library/Application Support/Google/Chrome/Default/History
- Linux: ~/.config/google-chrome/Default/History
2.	Run the Script:
- Clone the repository:
```
git clone https://github.com/Ian729/chrome-history-analysis.git
cd chrome-history-analysis
```
- Run the script:
```
python chrome_history_analysis.py
```
3. View Results:
- Top 10 visited URLs are displayed in the terminal.
- Most visited domains are saved in most_visited_domains.csv.