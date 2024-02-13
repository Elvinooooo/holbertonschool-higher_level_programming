#!/usr/bin/python3
"""Defines Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represrnts a Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the class
           Args:
                size(int): size of square
                x(int): x value
                y(int): y value
                id(int): unique id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width =  value
        self.height = value

    def __str__(self):
        """method that returns [Square] (<id>) <x>/<y> - <width>/<height>"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                    self.x, self.y,
                                                    self.size)
