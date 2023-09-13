#!/usr/bin/python3
"""
module with method is_same_class
"""


def is_same_class(obj, a_class):
    """Method that checks if object instance of class"""

    return type(obj) is a_class
