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
            my_print(self): Prints the square object
        """

    def __init__(self, size=0, position=(0, 0)):
        """
        The constructor of the Square class

        Args:
            size (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers ")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers ")
        self.__position = value

    def area(self):
        """
        calculates and returns the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character #
        or a new line if size is 0 print
        an empty line
        """
        if self.__size == 0:
            print()
        # print empty lines based on the position
        for i in range(self.__position[1]):
            print()
        # print the square
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
