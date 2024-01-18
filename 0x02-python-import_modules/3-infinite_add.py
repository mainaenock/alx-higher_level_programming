#!/usr/bin/python3
import sys
if __name__ == "__main__":
    numbers = sys.argv[1:]
    add = 0
    for arg in numbers:
        add = add + int(arg)
    print(add)
