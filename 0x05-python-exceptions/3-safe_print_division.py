#!/usr/bin/python3
def safe_print_division(a, b):
    x = None
    try:
        x = int(a) / int(b)
        return x
    except Exception as e:
        return (None)
    finally:
        print("{}{}".format("Inside result: ", x))
