#!/usr/bin/python3
"""Defines a function"""
import json


def from_json_string(my_str):
    """Function to convert json string to python object"""
    return json.loads(my_str)
