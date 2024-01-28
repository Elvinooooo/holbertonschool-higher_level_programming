#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multies = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multies.append(True)
        else:
            multies.append(False)

    return multies
