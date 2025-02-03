#!/usr/bin/python3
"""Defines a function called lookup that takes an argument obj"""


def lookup(obj):
    """Returns a list of all attributes and methods of the given object"""
    return dir(obj)
