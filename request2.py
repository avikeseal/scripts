#!/usr/bin/env bash python3 
import requests
from bs4 import BeautifulSoup

url = 'https://orlando.craigslist.org'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

#extract all the text from the page and print it
print(soup.get_text())
