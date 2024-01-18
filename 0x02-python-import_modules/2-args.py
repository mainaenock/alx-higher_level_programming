#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = len(sys.argv) - 1
    argus = sys.argv[1:]

    if total == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(total, '' if total == 1 else 's'))
        for i, arg in enumerate(argus, start=1):
            print("{}: {}".format(i, arg))

