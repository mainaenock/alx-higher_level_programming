#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    new = set(my_list)
    for i in new:
        total += i
    return total
