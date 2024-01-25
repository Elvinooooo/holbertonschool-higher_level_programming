#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
    print("{} is greater than 5".format(last_digit))
elif last_digit == 0:
    print("{} is 0".format(last_digit))
else:
    print("{} is less than 6 and not 0".format(last_digit))
