#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

"""
module of class BaseGeometry
"""


class Square(Rectangle):
    """Square class  inherits from Rectangle  inherits from BaseGeometry"""

    def __init__(self, size):

        """Method initailizes attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)

        self.__size = size

    def area(self):

        """area"""

        return self.__size ** 2
