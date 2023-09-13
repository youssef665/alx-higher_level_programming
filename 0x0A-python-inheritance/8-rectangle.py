#!/usr/bin/python3
"""Defines a class Rectangle  inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Represent a class  rectangle inherit from  BaseGeometry."""

    def __init__(self, width, height):
        """Intialize  new Rectangle.

        Args:
            width (int): The width
            height (int): The height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
