#!/usr/bin/python3
"""Module for printing squares.

This module provides a function that prints a square
made of the character '#'.
"""


def print_square(size):
    """Print a square using '#'.

    Args:
        size: length of the square sides (must be an integer).

    Returns:
        None

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)