#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for num1, num2 in zip(my_list_1, my_list_2):
        try:
            ans = num1 / num2
            result.append(ans)
