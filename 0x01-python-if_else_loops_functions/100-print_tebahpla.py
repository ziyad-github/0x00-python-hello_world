#!/usr/bin/python3
for letter in range(122, 96, -1):
    if (letter % 2 == 0):
        letter = chr(ord(letter) - 32)
    print(letter)
