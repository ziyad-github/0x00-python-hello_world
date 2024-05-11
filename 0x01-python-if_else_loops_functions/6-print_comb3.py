#!/usr/bin/python3
for num in range(100):
    for num2 in range(100, -1, -1):
        if sorted(str(num)) != sorted(str(num2)):
            if (num == 99):
                print("89")
                continue
            print("{}".format(num), end=", ")
