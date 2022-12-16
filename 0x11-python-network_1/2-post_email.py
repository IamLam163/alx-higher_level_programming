#!/usr/bin/python3
"""Script takes a URL and sends a POST request
with email as paramet"""

from sys import argv
#from urllib import request, parse
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
