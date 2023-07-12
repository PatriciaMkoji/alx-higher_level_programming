#!/usr/bin/python3
"""
Module doc
"""
import json
import os.path
import sys
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
json_list = []

if os.path.exists(filename):
    json_list = load_from_json_file(filename)

for idx in argv[1:]:
    json_list.append(idx)

save_to_json_file(json_list, filename)
