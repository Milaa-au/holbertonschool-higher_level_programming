#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    operations = (
        (add, "+"),
        (sub, "-"),
        (mul, "*"),
        (div, "/")
    )

    for func, symbol in operations:
        print(f"{a} {symbol} {b} = {func(a, b)}")
