#!/usr/bin/python3
"""ADd all arguments to pytohon list"""
import json


def save_to_json_file(my_obj, filename):
    """ save to python list function
        filename: the file name
    """

    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
