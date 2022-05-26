from bs4 import BeautifulSoup
import requests

PDS_WEBSITE_BASE = "https://pds-rings.seti.org/"
PDS_WEBSTIE_ALL_START = "https://pds-rings.seti.org/galleries/all_1986.html"

PDS_PRESS_RELEASES = "/press_releases/pages/"
HTML_EXT = ".html"
NEXT_PAGE_NAME = "next >"

to_scrape_links = [PDS_WEBSTIE_ALL_START]

while to_scrape_links:
    to_scrape_link = to_scrape_links.pop()
    
    website = requests.get(to_scrape_link)    
    soup = BeautifulSoup(website.content, 'html.parser')

    # Grab all links from the page
    links = soup.find_all('a')

    # Store all links to be scraped for images into a list
    target_links = []

    for link in links:
        website = link.get('href')
        
        if website:
            # add all press release pages to the target list
            if HTML_EXT in website and PDS_PRESS_RELEASES in website:
                target_links.append(website)
            # add all next pages to the scraping list  
            elif link.string == "next >":
                to_scrape_link.append(website)
                # print(website)