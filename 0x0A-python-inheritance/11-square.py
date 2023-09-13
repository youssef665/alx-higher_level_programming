#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

"""
module of class BaseGeometry
"""


class Square(Rectangle):
    """Square class  inherits from Rectangle class that inherits BaseGeometry class"""

    def __init__(self, size):

        """Method  initializes  attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """ area"""

        return self.__size ** 2

    def __str__(self):

        return "[Square] {}/{}".format(self.__size, self.__size)
