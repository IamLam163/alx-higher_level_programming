#!/usr/bin/python3
"""Script takes a URL, sends a request and displays
the body of the response"""

from sys import argv
from urllib import error
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
