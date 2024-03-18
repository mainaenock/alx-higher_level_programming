#!/usr/bin/python3
def element_at(my_list, idx):
    count = -1
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    for i in my_list:
        count += 1
        if count == idx:
            return i
