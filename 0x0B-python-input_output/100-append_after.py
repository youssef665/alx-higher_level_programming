#!/usr/bin/python3
"""Defines text file insert function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line.

    Args:
        filename (str): name of file
        search_string (str): The string to search
        new_string (str): The string to add
    """
    t = ""

    with open(filename) as s:
        for line in s:
            t += line

            if search_string in line:
                t += new_string

    with open(filename, "w") as wr:
        wr.write(t)
