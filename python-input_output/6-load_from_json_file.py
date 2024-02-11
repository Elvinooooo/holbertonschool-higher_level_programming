#!/usr/bin/python3
"""Defines a function"""
import json


def load_from_json_file(filename):
    """Function to convert json file to an object
        Args:
            filename -  the json file name to be converted
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
