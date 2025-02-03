#!/usr/bin/python3
"""
This module definies a class BaseGeometry
"""


class BaseGeometry():
    """
    Creates a Square class that inherits from Rectangle with a private
    attribute size, without getter or setter, validated as a positive
    integer by integer_validator. Implements the area() method and makes
    print() and str() return the description [Square] <width>/<height>
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

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
        """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
