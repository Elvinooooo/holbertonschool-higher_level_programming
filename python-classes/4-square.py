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
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Change the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size
