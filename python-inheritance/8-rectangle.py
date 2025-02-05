#!/usr/bin/python3
"""
This module definies a class BaseGeometry
"""


class BaseGeometry():
    """
    Creates a Rectangle class that inherits from BaseGeometry
    with private attributes width and height, without getter or setter,
    and which must be positive integers validated by integer_validator
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
        """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
