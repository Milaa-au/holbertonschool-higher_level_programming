#!/usr/bin/python3
"""Module for matrix division.

This module provides a function that divides all elements
of a matrix by a given number and returns a new matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix: list of lists of integers or floats.
        div: number (int or float) used as divisor.

    Returns:
        A new matrix with each element divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix is not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    row_length = None

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(error_msg)

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
