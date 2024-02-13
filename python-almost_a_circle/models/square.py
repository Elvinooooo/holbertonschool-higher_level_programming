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
        self.width = value
        self.height = value

    def __str__(self):
        """method that returns [Square] (<id>) <x>/<y> - <width>/<height>"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """Updating the attributes"""
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if len(kwargs) > 0:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of the square class"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
