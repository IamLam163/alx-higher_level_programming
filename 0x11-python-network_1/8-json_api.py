#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": letter}
    r = requests.post(url, data=payload)

    try:
        mydict = r.json()
        if mydict:
            print("[{}] {}".format(mydict.get("id"), mydict.get("name")))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
