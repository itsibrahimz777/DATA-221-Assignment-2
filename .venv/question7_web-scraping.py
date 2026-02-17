import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://en.wikipedia.org/wiki/Data_science"

# send GET request
response = requests.get(url)
html = response.text

# parse the HTML
soup = BeautifulSoup(html, "html.parser")

# extract and print page title
title = soup.find("title").text
print("Page Title:", title)

# find main content div
content_div = soup.find("div", id="mw-content-text")

# get first paragraph from the main content
first_paragraph = ""
for p in content_div.find_all("p"):
    text = p.get_text(strip=True)
    if len(text) >= 50:  # check length requirement
        first_paragraph = text
        break

# print the first paragraph
print("\nFirst Paragraph:")
print(first_paragraph)
