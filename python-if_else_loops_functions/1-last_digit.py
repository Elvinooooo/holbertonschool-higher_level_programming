#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lDig = abs(number) % 10
if number < 0:
	lDig *= -1
if lDig > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lDig))
elif lDig == 0:
    print("Last digit of {} is {} and is 0".format(number, lDig))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, lDig))
