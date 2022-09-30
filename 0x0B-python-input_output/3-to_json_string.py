#!/usr/bin/python3
"""
Contains function that returns JSON representation of obj as a (string)
"""


def to_json_string(my_obj):
    """Returns JSON representation of obj as a string
    Args:
        my_obj: python object
    Return:
        json string representation
    """

    return json.dumps(my_obj)
