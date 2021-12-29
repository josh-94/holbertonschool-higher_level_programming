#!/usr/bin/python3
for i in range(1, 90):
    if(i == 89):
        print("{:02d}".format(i))
        break
    if (i == 10 or i == 11):
        continue
    print("{:02d}".format(i), end=", ")
