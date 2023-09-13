#!/usr/bin/python3

"""Defines  student class ."""


class Student:

    """represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student.

        Args:
            first_name (str): The first name
            last_name (str): The last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """Get a dictionary representation."""
        return self.__dict__
