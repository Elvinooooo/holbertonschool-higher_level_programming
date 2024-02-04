#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """This class represents a Square
    This class can be used to create square objects.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square
        Args:
            int(size): the size of the square
            position(int, int): the position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Change the position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) for i in value) or \
           not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area"""
        return self.__size * self.__size

    def my_print(self):
        """Print # for each square"""
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
