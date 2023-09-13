#!/usr/bin/python3
"""
module with meth is_same_class
"""


def is_same_class(obj, a_class):
    """Method that checks if an object is an instances of class"""

    return type(obj) is a_class
