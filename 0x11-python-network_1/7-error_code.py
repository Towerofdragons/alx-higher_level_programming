#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    code = res.status_code
    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(res.text)
