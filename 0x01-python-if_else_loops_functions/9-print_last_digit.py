#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *=-1
        i = number % 10
    else:
        i = number % 10
    print(i, end='')
    return i
