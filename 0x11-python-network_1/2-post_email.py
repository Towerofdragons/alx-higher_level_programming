#!/usr/bin/python3
"""
Send POST request to URL with a provided email
"""
import urllib.parse, urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email":sys.argv[2]}
    encoded = urllib.parse.urlencode(values).encode("ascii")

    req = urllib.request.Request(url, encoded)

    with urllib.request.urlopen(req) as res:
        print (res.read().decode("utf-8"))
