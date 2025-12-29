#!usr/bin/env bash python3 
import requests
from bs4 import BeautifulSoup

#get a simple request from web page 
url = 'https://x.com'
response = requests.get(url)

#check to see if it works:
print(f'status code: {response.status_code}') #output should be 200
