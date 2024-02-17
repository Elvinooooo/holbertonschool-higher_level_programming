#!/usr/bin/python3
from models.rectangle import Rectangle
rec = Rectangle(1, 2)
print('Rectangle(1, "2") width result is: ', rec.width)
print('Rectangle(1, "2") height result is: ', rec.height)
print('Rectangle(1, 2, "3")  y result is:', rec.y)
print('Rectangle(1, 2, "3") x result is:', rec.x)
print("result id: ", rec.id)
