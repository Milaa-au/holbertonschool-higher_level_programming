#!/usr/bin/python3

number = 0
number2 = 0

for number in range(0, 10):
    for number2 in range(number + 1, 10):
        if number == 8 and number2 == 9:
            print(f"{number}{number2}")
        else:
            print(f"{number}{number2}", end=", ")
