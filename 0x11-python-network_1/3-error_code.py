#!/usr/bin/python3
""" Takes url and sends request to url """


import urllib.request
import urllib.error
from sys import argv

if __name__ == '__main__':
    try:
        url = argv[1]
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
