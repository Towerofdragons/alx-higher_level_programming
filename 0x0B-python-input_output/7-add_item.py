#!/usr/bin/python3
"""
Module defines function 'json_modify'
"""


if __name__ == "__main__":


    import json
    import sys


    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file= __import__("6-load_from_json_file").load_from_json_file


    filename = "add_item.json"
    try:
        obj = load_from_json_file(filename)
    except Exception:
        obj = []
        save_to_json_file(obj, filename)
    #print(obj)
    obj.extend(sys.argv[1:])
    #print(obj)
    save_to_json_file(obj, filename)



