#!/usr/bin/python3
"""Scrippt takes a URL and sends request and
displays the value from response header"""

from sys import argv
import requests

if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
