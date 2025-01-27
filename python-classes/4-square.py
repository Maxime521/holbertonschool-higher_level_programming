#!/usr/bin/python3
"""Square generation module for Python project
"""


class Square:
    """
    This is a class named Square with a private instance attribute size

    Attributes:
        size (int): The size of the square object

    Methods:
        __init__(self, size=0): The constructor of the Square class
        area(self): Returns the area of the square object
    """

    def __init__(self, size=0):
        """
        The constructor of the Square class

        Args:
            size (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """
        getter for the size attribute of the square class

        Returns:
            int: the size of the square object
        """
        return self.__size
        

    @size.setter
    def size(self, value):
        """
        setter for the size attribute of the square class

        Args:
            value (int): the size of the square object

        Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculates and returns the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2
