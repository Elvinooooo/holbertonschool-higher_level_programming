#!/usr/bin/python3
"""Defines MyList that inherits from list"""


class MyList(list):
    """MyList inherited from the list"""

    def print_sorted(self):
        """Print the sorted list"""
        print(sorted(self))
