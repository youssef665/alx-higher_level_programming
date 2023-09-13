#!/usr/bin/python3

"""Defines a JSON file read function."""

import json


def load_from_json_file(filename):

    """Create a Python object."""

    with open(filename) as f:
        return json.load(f)
