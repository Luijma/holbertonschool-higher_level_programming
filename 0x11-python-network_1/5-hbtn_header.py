#!/usr/bin/python3
""" takes url sends request to url and displays x-request-id """


import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    request = requests.get(url)
    print(request.headers.get('X-Request-Id'))
