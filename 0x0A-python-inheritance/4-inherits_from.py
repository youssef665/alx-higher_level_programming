#!/usr/bin/python3

"""
module with meth inherits_from
"""


def inherits_from(obj, a_class):
    """Methid checks if an object is an instance of a class
    that inherited  from directly or undirectly"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
