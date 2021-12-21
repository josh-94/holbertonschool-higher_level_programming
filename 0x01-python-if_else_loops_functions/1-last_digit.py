#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    renum = number % -10
else:
    renum = number % 10
print("Last digit of {:d} is {:d}".format(number, renum), end=" ")
if((renum) > 5):
    print("and is greater than 5")
elif((renum) == 0):
    print("and is 0")
elif((renum) < 6 and not 0):
    print("and is less than 6 and not 0")
