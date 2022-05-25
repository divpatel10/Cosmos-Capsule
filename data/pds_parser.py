from bs4 import BeautifulSoup
import requests

PDS_WEBSTIE_BASE = "https://pds-rings.seti.org"
PDS_GALLERY_BASE = "/galleries"
HTML_EXT = ".html"

IGNORE_LINK_NAMES = {"<< first", "< previous"}
IGNORE_LINK_HREF = {"/galleries.html"}
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


links_to_scrape = []
try:
    for link in target_links:
        website = requests.get(link)

        soup = BeautifulSoup(website.content, 'html.parser')
        links = soup.find_all('a')
        for l in links:
                if l.string and l.string not in IGNORE_LINK_NAMES:
                    if "html" in l.get('href') and l.get('href') not in IGNORE_LINK_HREF:
                        links_to_scrape.append(l.get('href'))
except:
    print(f"error scraping link {link}")

for l in links_to_scrape:
    print(l)