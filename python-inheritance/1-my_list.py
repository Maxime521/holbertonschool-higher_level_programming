#!/usr/bin/python3
""" Defines a class 'MyList' that inherits from the built-in 'list' class
    The class 'MyList' extends the behavior of the built-in list class to include new functionalities"""


class MyList(list):
    """ Method that prints the sorted version of the list, added to MyList
        Uses sorted() to create a sorted version of the list, then prints it
    """
    def print_sorted(self):
        print(sorted(self))
