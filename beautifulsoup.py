#!usr/bin/env bash python3 
import requests
from bs4 import BeautifulSoup

#get a simple request from web page 
url = 'https://api.github.com'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

#check to see if it works:
print('soup.title)
print(f'status code: {response.status_code}') #output should be 200
