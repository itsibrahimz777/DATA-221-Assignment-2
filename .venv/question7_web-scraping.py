import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

# add User-Agent header
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# extract title safely
title_tag = soup.find("title")
if title_tag:
    title = title_tag.text
    print("Page Title:", title)
else:
    print("Title tag not found. Page may be blocked or HTML changed.")

# extract first paragraph
content_div = soup.find("div", class_="mw-parser-output")

if content_div:
    first_paragraph = ""
    for p in content_div.find_all("p"):
        text = p.get_text(strip=True)
        if len(text) >= 50:
            first_paragraph = text
            break
    print("\nFirst Paragraph:")
    print(first_paragraph)
else:
    print("Main content not found.")

