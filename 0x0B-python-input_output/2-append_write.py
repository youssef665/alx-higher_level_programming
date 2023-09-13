#!/usr/bin/python3
"""Defines a file append function."""


def append_write(filename="", text=""):
    """Appends a string file.

    Args:
        filename (str): The name of the file
        text (str): The string to append
    Returns:
        The number of chars.
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
