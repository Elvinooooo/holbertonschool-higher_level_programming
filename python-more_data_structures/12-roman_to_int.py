#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0
    roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    for i in range(0, len(roman_string)):
        for key in roman_numerals.keys():
            if key == roman_string[i]:
                result += roman_numerals[key]
    return result
