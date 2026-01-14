#!/usr/bin/python3
def fizzbuzz():
    for a in range (100):
	    if a % 3 == 0 and a % 5 == 0:
		    print("FizzBuzz")
	    elif a % 5 == 0:
		    print("Buzz")
	    elif a % 3 == 0:
		    print("Fizz")
	    else:
		    print(a)
	    if (a < 100):
		    print(" ")