#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    sq = []
    for i in new:
        sqr = list(map(lambda x: x**2, i))
        sq.append(sqr)
    return sq
