#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if (ord("a") <= ord(letter) < ord("z")):
            print("{}".format(chr(ord(letter) - 32)), end="")
        else:
            print("{}".format(letter), end="")
