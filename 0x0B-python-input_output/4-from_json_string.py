#!/usr/bin/python3
"""Defines  a JSON  function."""

import json


def from_json_string(my_str):
    """Return the Python object representation."""

    return json.loads(my_str)
