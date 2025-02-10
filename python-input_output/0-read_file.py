#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF-8 encoded) and prints its content to stdout.

    Args:
        filename (str): The path to the file to be read. Defaults to an empty string.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
