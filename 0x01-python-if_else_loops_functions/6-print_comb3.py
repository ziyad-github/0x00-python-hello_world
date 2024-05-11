#!/usr/bin/python3
for num in range(100):
    for num2 in range(100, -1, -1):
        if (sorted(str(num)) == sorted(str(num2))):
            break
        else:
            if (num == 99):
                print("89")
                continue
            print("{:02d}".format(num), end=", ")
