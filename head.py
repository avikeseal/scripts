#!usr/bin/env bash python3
from bs4 import BeautifulSoup
import requests

url = "https://tutorialspoint.com"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

soup.prettify()
print(soup.head)
