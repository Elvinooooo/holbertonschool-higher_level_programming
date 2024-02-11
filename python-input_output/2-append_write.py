#!/usr/bin/python3
"""Module with the function for appending text to a file"""


def append_write(filename="", text=""):
    """Function that opens file and appends the text at the end
        Args:
            filename: string of file name
            text: text to be added inside the file

        Return: Number of characters of written text
    """

    with open(filename, "a", encoding="utf-8") as f:
        length = f.write(text)
        return length
