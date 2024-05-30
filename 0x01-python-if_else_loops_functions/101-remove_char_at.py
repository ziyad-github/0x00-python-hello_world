#!/usr/bin/python3
def remove_char_at(str, n):
    array = list(str)
    if (len(array) <= n or n < 0):
        return str
    array.pop(n)
    return ''.join(array)
