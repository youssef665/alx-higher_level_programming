#!/usr/bin/python3

"""Defines a function that adds attributes"""


def add_attribute(obj, att, value):

    """Add a new attribute

    Args:
        obj (any): The object to add
        att (str): The name of the attributes
        value (any): The value
    Raises:
        TypeError: If the attribute not added.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
