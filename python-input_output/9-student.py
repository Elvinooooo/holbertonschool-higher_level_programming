#!/bin/usr/python3
"""Defines a Student class"""


class Student:
    """Represents Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize the class

        Args:
            first_name (str): The first name of the student.
            last_name (str): The surname of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Convert to json dict"""
        return self.__dict__ 
