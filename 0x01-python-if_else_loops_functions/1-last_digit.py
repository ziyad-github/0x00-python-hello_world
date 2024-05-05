#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_n = abs(number % 10)
print(f"Last digit of {number:d} is ", end="")
if number < 0:
    print(f"-{digit:d} and is ", end="")
if digit == 0:
    print("zero")
elif digit < 6:
    print("less than 6 and not 0")
else:
    print("greater than 5")
