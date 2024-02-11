#!/usr/bin/python3
"""Defines a function"""
import json


def save_to_json_file(my_obj, filename):
    """Function to convert object to json string then write it into file
        Args:
            my_obj -  objecct to be converted
            filename -  the file to be written inside
    """
    with open(filename, "w", encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
