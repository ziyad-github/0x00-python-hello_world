#!/usr/bin/python3
for num in range(100):
    if (num == 99):
        print("{:d}".format(num))
        continue
    print("{:02d}".format(num), end=", ")
