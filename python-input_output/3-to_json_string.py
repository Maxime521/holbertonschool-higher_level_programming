#!/usr/bin/python3
"""
This module defines a function to_json_string
that returns the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
