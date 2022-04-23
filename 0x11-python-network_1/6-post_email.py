#!/usr/bin/python3
""" Takes url and email address and sends POST request """


import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}
    request = requests.post(url, values)
    print(request.text)
