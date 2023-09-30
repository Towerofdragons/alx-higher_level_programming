#!/usr/bin/python3
"""
Fetch https://alx-intranet.hbtn.io/status using urllib
"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        res =  response.read()
        print("Body response:")
        print(f"\t- type: {type(res)}\n\t- content: {res}\n\t- utf8 content: {res.decode('utf-8')}")
