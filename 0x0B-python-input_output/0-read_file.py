#!/usr/bin/python3
"""Defines  text file read only function."""


def read_file(filename=""):

    """Print the contents of a file."""
    with open(filename,"r", encoding="UTF-8") as f:
        print(f.read(), end="")
