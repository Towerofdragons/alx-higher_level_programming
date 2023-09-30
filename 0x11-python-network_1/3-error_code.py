#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request, urllib.error
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode("ascii"))
    except urllib.error.HTTPError as err:
            print(f"Error code: {err.code}")
