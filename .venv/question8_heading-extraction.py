import requests
from bs4 import BeautifulSoup

# URL
url = "https://en.wikipedia.org/wiki/Data_science"

# ✅ Add User-Agent header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# request page
response = requests.get(url, headers=headers)
response.raise_for_status()  # helps detect request errors

soup = BeautifulSoup(response.text, "html.parser")

# ✅ Updated main content selector
content_div = soup.find("div", class_="mw-parser-output")

if content_div is None:
    print("Main content not found.")
    exit()

# words to exclude
exclude_words = ["References", "External links", "See also", "Notes"]

headings = []

# extract all h2 tags inside main content
for h2 in content_div.find_all("h2"):
    heading_text = h2.get_text(strip=True)

    # remove [edit]
    heading_text = heading_text.replace("[edit]", "")

    # skip unwanted headings
    if any(word in heading_text for word in exclude_words):
        continue

    headings.append(heading_text)

# save to file
with open("headings.txt", "w", encoding="utf-8") as file:
    for heading in headings:
        file.write(heading + "\n")

print("Headings saved to headings.txt")
