#!/usr/bin/python3
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        print("{}{:}".format(tens_digit, ones_digit), end="")
        if tens_digit < 8 or ones_digit < 9:
            print(", ", end="")
print()
