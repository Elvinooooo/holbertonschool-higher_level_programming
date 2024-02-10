#!/usr/bin/python3
"""Defines lookup function for the object attribute"""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

        Args:
        - obj: The object whose attributes and methods are to be listed.

         Returns:
        - list: A list of strings of attributes and methods of the object.
    """
    return (dir(obj))
