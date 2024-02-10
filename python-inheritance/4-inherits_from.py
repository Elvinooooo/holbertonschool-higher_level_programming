#!/usr/bin/python3
"""Defines a class comparison"""


def inherits_from(obj, a_class):
    """ if obj is an instance of a class that inherited from given class

    Args:
        obj: Object to be compared
        a_class: the class to be checked

    Return: True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
