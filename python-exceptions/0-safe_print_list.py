#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    quantity = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            quantity += 1
        print()
        return quantity
    except IndexError:
        print()
        return quantity
