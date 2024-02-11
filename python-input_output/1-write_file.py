#!/usr/bin/python3
"""Module with the function for writin file"""


def write_file(filename="", text=""):
    """Function that opens file and writes the text
        Args:
            filename: string of file name
            text: text to be written inside the file

        Return: Number of characters of written text
    """

    with open(filename, "w", encoding="utf-8") as f:
        length = f.write(text)
        return length
