# Import and load necessary lib
from bs4 import BeautifulSoup
import requests


def extract_jobs_url(soup):
    fb_url = "https://www.facebook.com"
    jobs_links = []
    list_jobs_links = []
    jobs_list = soup.find("div", {"class": "_8tk7"})
    jobs = jobs_list.find_all("a", {"class": "_8sef"})
    links = [link['href'] for link in jobs]
    jobs_links = links
    for link in jobs_links:
        list_jobs_links.append(fb_url+link)
        # Need to push to a db
    print(list_jobs_links)
    return list_jobs_links

def extract_jobs_title(soup):
    jobs_titles = []
    list_jobs_titles = []
    jobs_list = soup.find("div", {"class": "_8tk7"})
    jobs = jobs_list.find_all("div", {"class": "_8sel"})
    jobs_titles = jobs
    for title in jobs_titles:
        list_jobs_titles.append(title.get_text())
        # Need to push to a db
    print(list_jobs_titles)
    return list_jobs_titles

def create_soup(req):
    print(req.status_code)
    soup = BeautifulSoup(req.content, 'html.parser')
    # print(soup.prettify())
    return soup

def create_req():
    # Load our first page
    # Need to pull from db
    search_url = "https://www.facebook.com/careers/jobs/?q="
    prefrences = "DevOps"
    req = requests.get(search_url+prefrences)
    return req
