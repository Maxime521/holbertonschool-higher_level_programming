#!/usr/bin/python3
"""
This module definies a class BaseGeometry
"""


class BaseGeometry():
    """
    Create a class BaseGeometry with a public method area that raises
    an exception with the message "area() is not implemented"
    and a method integer_validator that validates an integer
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
