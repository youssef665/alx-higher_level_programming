#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
module of class BaseGeometry
"""


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Method initalizes  attrubutes"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):

        """Method to define again area method in parent class"""

        return self.__width * self.__height

    def __str__(self):

        """__str__ method  return the  string after"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
