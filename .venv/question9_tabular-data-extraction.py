import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Machine_learning"

# ✅ Add browser header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

content_div = soup.find("div", class_="mw-parser-output")

if content_div is None:
    print("Main content not found.")
    exit()

tables = content_div.find_all("table")

selected_table = None

for table in tables:
    rows = table.find_all("tr")
    data_rows = [row for row in rows if row.find("td")]

    if len(data_rows) >= 3:
        selected_table = table
        break

if selected_table is None:
    print("No suitable table found.")
    exit()

rows = selected_table.find_all("tr")

# Extract headers
header_cells = rows[0].find_all("th")

if header_cells:
    headers = [cell.get_text(strip=True) for cell in header_cells]
else:
    max_cols = max(len(row.find_all(["td", "th"])) for row in rows)
    headers = [f"col{i + 1}" for i in range(max_cols)]

max_cols = len(headers)

table_data = []

for row in rows[1:]:
    cells = row.find_all(["td", "th"])
    if not cells:
        continue

    row_data = [cell.get_text(strip=True) for cell in cells]

    while len(row_data) < max_cols:
        row_data.append("")

    table_data.append(row_data)

with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(table_data)

print("Table successfully saved to wiki_table.csv")
