#!/usr/bin/python3
def islower(c):
    a = 97
    A = 65
    if (a < ord(c) < a + 26):
        return True
    else:
        return False
