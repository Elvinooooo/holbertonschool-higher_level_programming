#!/usr/bin/python3
"""Define a Square class """


class Square:
    """This class represents a Square.

    This class can be used to create square objects.
    """
    def __init__(self, size=0):
        """Initialize a Square object with a given size
        Args:
            size(int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
