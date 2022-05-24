from bs4 import BeautifulSoup
import requests

PDS_WEBSTIE_BASE = "https://pds-rings.seti.org"
PDS_GALLERY_BASE = "/galleries"
HTML_EXT = ".html"

website = requests.get(PDS_WEBSTIE_BASE + PDS_GALLERY_BASE + HTML_EXT)

soup = BeautifulSoup(website.content, 'html.parser')

# Grab all links from the base page
links = soup.find_all('a')

# Store all links to be scraped for images into a list
target_links = []
for link in links:
    href = link.get('href')
    if href and "galleries/" in href:
        target_links.append(PDS_WEBSTIE_BASE + href)

