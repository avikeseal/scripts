#!/usr/bin/env bash python3
import requests

url = "https://api.github.com/events"

response = requests.get(url)
print(response)
