#!/usr/bin/python3
"""
Module defines function 'load_from_json'
"""


import json


def load_from_json_file(filename):
    """
    A function that creates an Object from a “JSON file”
    """
    
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
