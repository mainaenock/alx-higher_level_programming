#!/usr/bin/python3
"""
This module divides matrix by a number div
the div must be either an int or a float
"""
def matrix_divided(matrix, div):
    len_matrix = len(matrix[0])
    for row in matrix:
        if not isinstance(row, (list)):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        for num in row:
            if not isinstance(num,(int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix[1:]:
        if len(row) != len_matrix:
            raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    result = []
    for row in matrix:
        results = [round((num / div), 2) for num in row]
        result.append(results)
    return result
