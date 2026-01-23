#!/usr/bin/python3

"""
This module provides a function to divide all elements of a matrix.

The matrix must be a list of lists containing integers or floats.
Each row of the matrix must have the same size.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): Matrix of integers or floats
        div (int or float): Divider for all elements of the matrix

    Returns:
        list of lists: A new matrix with all elements divided by div
        and rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        TypeError: If rows of the matrix are not of the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is equal to zero
    """

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