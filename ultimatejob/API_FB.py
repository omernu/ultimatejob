# Import and load necessary lib

import requests
import bs4
from bs4 import BeautifulSoup as bs
import re

# Load our first page

search_url = "https://www.facebook.com/careers/jobs/?q="
fb_url = "https://www.facebook.com"

prefrences = "DevOps" # Need to pull from db
r = requests.get(search_url+prefrences)

# Checking if content is available
#print(r.status_code)

soup = bs(r.content)
#print(soup.prettify())

# Manipulation

def extract_jobs_list(soup):
    jobs_links = []
    jobs_list = soup.find("div", {"class": "_8tk7"})
    jobs = jobs_list.find_all("a", {"class": "_8sef"})
    links = [link['href'] for link in jobs]
    titles = jobs_list.find_all("div", {"class": "_8sel _97fe"})
    jobs_links = links
    for l in jobs_links:
        print(fb_url+l)
    
def extract_jobs_title(soup):
    jobs_titles = []
    jobs_list = soup.find("div", {"class": "_8tk7"})
    jobs = jobs_list.find_all("div", {"class": "_8sel"})
    jobs_titles = jobs
    for l in jobs_titles:
        print(l.get_text())

extract_jobs_list(soup)
extract_jobs_title(soup)
