#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elm in row:
            print("{}".format(elm), end=" ")
        print()
