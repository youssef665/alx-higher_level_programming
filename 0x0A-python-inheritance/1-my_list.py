#!/usr/bin/python3
"""Defines an inherited class MyList."""


class MyList(list):
    """Implements sorted lists"""

    def print_sorted(self):
        """Print a list in  ascending order."""

        print(sorted(self))
