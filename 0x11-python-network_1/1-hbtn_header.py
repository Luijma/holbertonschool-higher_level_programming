#!/usr/bin/python3
""" Takes url, sends request to URL """


import urllib.request
from sys import argv

if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as response:
        header = response.info()

    print(header.get('X-Request-Id'))
