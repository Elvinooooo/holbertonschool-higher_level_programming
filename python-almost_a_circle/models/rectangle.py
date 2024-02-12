#!/usr/bin/python3
"""Defines a rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represent Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the class
        Args:
            width(int): width of rectangle
            height(int): height of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/Get the width"""
        return self.__width

    @property
    def height(self):
        """Set/Get the height"""
        return self.__height

    @property
    def x(self):
        """Set/Get the x value"""
        return self.__x

    @property
    def y(self):
        """Set/Get the y value"""
        return self.__y
