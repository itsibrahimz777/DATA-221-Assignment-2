import requests
from bs4 import BeautifulSoup
import csv

# URL
url = "https://en.wikipedia.org/wiki/Machine_learning"

# request page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# find main content area
content_div = soup.find("div", id="mw-content-text")

# find all tables inside main content
tables = content_div.find_all("table")

selected_table = None

# locate first table with at least 3 data rows
for table in tables:
    rows = table.find_all("tr")

    # count rows that contain <td> (data rows)
    data_rows = [row for row in rows if row.find_all("td")]

    if len(data_rows) >= 3:
        selected_table = table
        break

if selected_table is None:
    print("No suitable table found.")
else:
    rows = selected_table.find_all("tr")

    # extract header
    header_row = rows[0].find_all("th")

    if header_row:
        headers = [th.get_text(strip=True) for th in header_row]
    else:
        # determine max number of columns
        max_cols = max(len(row.find_all(["td", "th"])) for row in rows)
        headers = [f"col{i + 1}" for i in range(max_cols)]

    # extract data rows
    table_data = []
    max_cols = len(headers)

    for row in rows[1:]:
        cells = row.find_all(["td", "th"])
        if not cells:
            continue

        row_data = [cell.get_text(strip=True) for cell in cells]

        # pad missing values
        while len(row_data) < max_cols:
            row_data.append("")

        table_data.append(row_data)

    # save to CSV
    with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(table_data)

    print("Table saved to wiki_table.csv")
