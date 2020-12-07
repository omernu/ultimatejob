### Import and load necessary lib

import requests
import bs4
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

### Load our first page

devops_origin_url = "https://www.facebook.com/careers/jobs/?q=devops"
search_url = "https://www.facebook.com/careers/jobs/?q="
#prefrences = "DevOps" # Need to pull from db
r = requests.get(devops_origin_url)
#r = requests.get(search_url+prefrences)

### Checking if content is available
#print(r.status_code)

soup = bs(r.content)
#print(soup.prettify())

# Manipulation

#links = soup.find_all("a")
#links

fb_url = "https://www.facebook.com"

jobs_list = soup.find("div", {"class": "_8tk7"})
jobs = jobs_list.find_all("a", {"class": "_8sef"})
links = [link['href'] for link in jobs]
titles = jobs_list.find_all("div", {"class": "_8sel _97fe"})
links