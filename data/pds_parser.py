from bs4 import BeautifulSoup
import requests
import asyncio

PDS_WEBSITE_BASE = "https://pds-rings.seti.org/galleries/"
PDS_WEBSTIE_ALL_START = "https://pds-rings.seti.org/galleries/all_1986.html"

PDS_PRESS_RELEASES = "/press_releases/pages/"
HTML_EXT = ".html"
NEXT_PAGE_NAME = "next >"

to_scrape_links = [PDS_WEBSTIE_ALL_START]

# Store all links to be scraped for images into a list
target_links = []

visited = set()
while to_scrape_links:
    to_scrape_link = to_scrape_links.pop()

    if to_scrape_link in visited:
        print(f"{to_scrape_link} has been already visited")
        continue

    visited.add(to_scrape_link)

    website = requests.get(to_scrape_link)    
    soup = BeautifulSoup(website.content, 'html.parser')

    # Grab all links from the page
    links = soup.find_all('a')

    for link in links:
        website = link.get('href')
        
        if website:
            # add all press release pages to the target list
            if HTML_EXT in website and PDS_PRESS_RELEASES in website:
                target_links.append(website)
            # add all next pages to the scraping list  
            elif link.string == NEXT_PAGE_NAME:
                to_scrape_links.append(PDS_WEBSITE_BASE + website)
