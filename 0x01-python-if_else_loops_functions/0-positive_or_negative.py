#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    printf(f"{number:d} is positive")
elif number == 0:
    printf(f"{number:d} is zero")
else:
    printf(f"{number:d} is negative")
