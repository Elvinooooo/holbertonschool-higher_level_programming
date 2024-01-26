#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 65:
            c = chr(ord(c) - 32)
            print("{}".format(c), end="")
    print()
