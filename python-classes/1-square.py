#!/usr/bin/python3
"""Define a Square class """


class Square:
    """Define a Square class.

    This class represents a square and can be used to create square objects.
    """
    def __init__(self, size):
        """Initialize a Square object with a given size
        Args:
            size(int): the size of the square
        """
        self.__size = size
