#!/usr/bin/python3
"""Defines student class."""


class Student:

    """Represent  student."""

    def __init__(self, first_name, last_name, age):
        """Initialize  student.

        Args:
            first_name (str): The first name
            last_name (str): The last name
            age (int): Age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary represen.

        If attrs is a list of strings, represents only attribu

        Args:
            attrs (list): (Optional) The attributes
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
