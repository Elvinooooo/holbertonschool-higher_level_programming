#!/usr/bin/python3
"""Module with the function for reading file"""


def read_file(filename=""):
    """Function that opens file and prints its content"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
