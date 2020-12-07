### Import and load necessary lib

import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import re

Load our first page

devops_origin_url = "https://www.facebook.com/careers/jobs/?q=devops"

search_url = "https://careers-redhat.icims.com/jobs/search?ss=1&searchKeyword="

#prefrences = "DevOps" # Need to pull from db

r = requests.get(devops_origin_url)
#r = requests.get(search_url+prefrences)

### Checking if content is available
#print(r.status_code)

soup = bs(r.content)
print(soup.prettify())

### Manipulation

## Using find-all func

#title = webpage.find_all('a', attrs={'title': '82172 - Data Engineer Consultant'})
#title.text

#results = soup.find(class='iCIMS_Anchor')
#print(results.prettify())

## Using find func

#results = soup.find(id='container-fluid iCIMS_JobsTable')
#link = soup.find("a")
#link['href']

links = webpage.find_all(string=re.compile("http"))
links

content = soup.select("div p")
content

### Filter only http

actual_links = [link['href'] for link in links2]
actual_links

# USEFULL under list "ul" named fun-facts print contains "is"

facts = webpage.select("ul.fun-facts li")
facts_with_is = [fact.find(string=re.compile("is")) for fact in facts]
facts_with_is = [fact.find_parent().get_text() for fact in facts_with_is if fact]
facts_with_is

# USEFULL links with "Marketing" 

for link in links:
    if "Marketing" in link.text:
          print(link)
          print(link.attrs['href'])