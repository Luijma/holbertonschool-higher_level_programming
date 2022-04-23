#!/usr/bin/python3
""" Sends POST request to url with letter as a parameter """


from sys import argv
import requests

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"

    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    values = {'q': q}

    request = requests.post(url, values)

    try:
        json_obj = request.json()
        if json_obj:
            print("[{}] {}".format(json_obj.get("id"), json_obj.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
