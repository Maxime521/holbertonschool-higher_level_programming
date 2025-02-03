#!/usr/bin/python3
"""
Function that checks if an object is an instance
of a class or an instance of a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    """ Defines a function named is_kind_of_class that takes two arguments: obj and a_class.
        Returns True if obj is an instance of a_class (or a subclass of it), otherwise False.
    """
    return isinstance(obj, a_class)
