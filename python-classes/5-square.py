#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """This class represents a Square
    This class can be used to create square objects.
    """
    def __init__(self, size=0):
        """Initialize a square
        Args:
            int(size): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """Retrieve size"""
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
        """Return the area"""
        return self.__size * self.__size

    def my_print(self):
        """Print # for each square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
