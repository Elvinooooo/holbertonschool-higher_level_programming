#!/usr/bin/python3
""" define a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
    - matrix (list of lists): The matrix to be divided. Must contain integers or floats.
    - div (int or float): The divisor.

    Returns:
    - list of lists: A new matrix where each element is divided by the divisor, rounded to 2 decimal places.

    Raises:
    - TypeError: If matrix is not a list of lists of integers or floats, or if div is not a number.
    - TypeError: If each row of the matrix does not have the same size.
    - ZeroDivisionError: If div is equal to zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) \
            or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
