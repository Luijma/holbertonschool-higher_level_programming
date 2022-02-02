#!/usr/bin/python3
""" adds arguments to python list and saves them
"""


import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = 'add_items.json'
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []
new_items = sys.argv[1:]
items.extend(new_items)

save_to_json_file(items, filename)
