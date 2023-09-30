#!/usr/bin/python3
"""
Takes in a letter and sends a POST request 
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    param = "" if len(sys.argv) < 2 else sys.argv[1]
    res = requests.post("http://0.0.0.0:5000/search_user", data={'q': param})

    try:
        print(res.json())
        if response == {}:
            print("No result")
        else:
            print(f"[{res.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
