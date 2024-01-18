#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    addd = add(a, b)
    subb = sub(a, b)
    mull = mul(a, b)
    divv = div(a, b)
    print("{} + {} = {}".format(a, b, addd))
    print("{} - {} = {}".format(a, b, subb))
    print("{} * {} = {}".format(a, b, mull))
    print("{} / {} = {}".format(a, b, divv))
