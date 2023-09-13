#!/usr/bin/python3
"""Defines a file write  function."""


def write_file(filename="", text=""):
    """Write a string to  file.

    Args:
        filename (str): The name of the file
        text (str): The text to be written
    Returns:

        The number of char
    """
    with open(filename, "w", encoding="utf-8") as f:

        return f.write(text)
