#!/usr/bin/python3
""" Takes url sends requests and gets errorcode from header """


from sys import argv
import requests

if __name__ == '__main__':
    url = arv[1]
    request = requests.get(url)
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
