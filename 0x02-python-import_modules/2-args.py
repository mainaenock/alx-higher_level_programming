#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = (len(argv) - 1)
    count = 1
    if a == 0:
        print("{}".format("0 arguments."))
    elif a ==1:
        print("{}\n{}: {}".format("1 argument:", 1, argv[1]))
    else:
        print("{} {}".format(a,"arguments:"))
        for i in argv[1:]:
            print("{}: {}".format(count, i))
            count += 1

