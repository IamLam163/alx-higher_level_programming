#!/usr/bin/python3
"""Scrippt takes a URL and sends request and
displays the value pf X-Request-Id variable"""

from sys import argv
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
