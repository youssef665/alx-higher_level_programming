#!/usr/bin/python3
"""Defines  text file read only function."""


def read_file(filename=""):

    """Print the contents of a file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
