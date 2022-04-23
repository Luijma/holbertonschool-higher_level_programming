#!/usr/bin/python3
""" uses github credentials to display id """


import requests
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    url = "https://api.github.com/user"
    request = requests.get(url, auth=(user, password))
    print(request.json().get("id"))
