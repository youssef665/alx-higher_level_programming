#!/usr/bin/python3

"""
Module of class mylist
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Methot  sorts a list"""

        print(sorted(list(self)))
