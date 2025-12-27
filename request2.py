#!/usr/bin/env bash python3 
import requests
from bs4 import BeautifulSoup

url = 'https://orlando.craigslist.org'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

#extract the title  from the page and print it
print('title of the page: ')
print(soup.title)
