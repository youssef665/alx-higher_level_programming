#!/usr/bin/python3

"""Defines  LockedClass"""


class LockedClass:

    """
    Prevents the user from creating new instance

    Attributes:
        first_name (str): first name
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances """

        self.first_name = "first_name"
