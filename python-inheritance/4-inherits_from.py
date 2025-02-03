#!/usr/bin/python3
"""
This module contains a function inherits_from that checks if an object is an instance
of a class that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """ Defines a function called inherits_from that takes two parameters: obj and a_class
        Returns True if obj is an instance of a_class, but not exactly of that class (i.e., it's a subclass)
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
