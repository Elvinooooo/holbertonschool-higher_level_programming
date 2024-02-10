#!/usr/bin/python3
"""Defines a Square class inheriting from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square class"""

    def __init__(self, size):
        """Initialize the Rectangle
            Args:
                size: positive integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
