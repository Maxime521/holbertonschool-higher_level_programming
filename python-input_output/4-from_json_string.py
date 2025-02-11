#!/usr/bin/python3
"""
This module defines a function from_json_string
that returns an object represented by a JSON string.
"""


import json


def from_json_string(my_str):
    return json.loads(my_str)
