#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = tuple(x + y for x, y in zip(tuple_a, tuple_b))
    return new
