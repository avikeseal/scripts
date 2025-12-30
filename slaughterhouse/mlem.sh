#!usr/bin/env bash

echo "response from the web page: "
echo "==========================="

# http method to get headers and save it inside a file:
curl -o mlem.txt -X GET "https://httpbin.org/headers" \
-H "accept: application/json"

#displays the content of the file:
cat mlem.txt
