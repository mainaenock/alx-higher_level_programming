#!/usr/bin/python3
"""
This module multiplies 2 matrices
"""
def matrix_mul(m_a, m_b):
    """
    This function takes 2 parameters to represent the 2 matrices
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    a_len = len(m_a[0])
    b_len = len(m_b[0])
    for row in m_a:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError('m_b should contain only integers or floats')
    for row in m_a[1:]:
        if a_len != len(row):
            raise TypeError('each row of m_a must be of the same size')
    for row in m_b[1:]:
        if b_len != len(row):
            raise TypeError('each row of m_b must be of the same size')
    if a_len != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0] * len(m_b[0]) for _ in range(len(m_a))]
    
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    
    return result
