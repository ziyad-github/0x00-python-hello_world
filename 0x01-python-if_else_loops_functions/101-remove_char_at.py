#!/usr/bin/python3
def remove_char_at(str, n):
    array = list(str)
    if (len(array) <= n):
        return str
    array = array.pop(n)
    return ''.join(array)
