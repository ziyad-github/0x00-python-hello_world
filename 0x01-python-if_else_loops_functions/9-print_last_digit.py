#!/usr/bin/python3
def print_last_digit(number):
    last_d = abs(number) % 10
    print("{:d}".format(last_d))
    return last_d
