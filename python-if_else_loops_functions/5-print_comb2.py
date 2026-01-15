#!/usr/bin/python3

number = 0

for i in range(0, 100):
    if number != 99:
        print("{:02}".format(number), end=", ")
    if number == 99:
        print("{}\n".format(number))
    number = number + 1
