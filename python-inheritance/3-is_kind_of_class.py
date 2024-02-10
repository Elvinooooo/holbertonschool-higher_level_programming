#!/usr/bin/python3
"""Defines a class comparison"""


def is_kind_of_class(obj, a_class):
    """Function that checks whether istance is derived from class

    Args:
        obj: Object to be compared
        a_class: the class to be checked

    Return: True or False
    """
    return isinstance(obj, a_class)
