#!/usr/bin/python3
"""
contains function that appends to text file and returns numbers and char
"""


def append_write(filename="", text=""):
    """appends to existing text file and returns number and char added"""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
