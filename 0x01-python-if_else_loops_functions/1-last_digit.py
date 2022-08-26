#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
figure = int(repr(number)[-1])
print("Last digit of {} is {} and is ".format(number, figure), end="")
if figure < 0:
	figure = -figure
if figure > 5:
	print("greater than 5")
elif figure == 0:
	print("0")
else:
	print("less than 6 and not 0")
