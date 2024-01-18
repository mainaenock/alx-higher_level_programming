#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = len(sys.argv) - 1
    argus = sys.argv[1:]
    if total == 1:
        print("1 argument:")
        for i, arg in enumerate(argus, start=1):
            print("{}: {}".format(i, arg))
    elif total > 1:
        print("{} arguments:".format(total))
        for i, arg in enumerate(argus, start=1):
            print("{}: {}".format(i,arg))
    else:
            print("0 arguments.")
