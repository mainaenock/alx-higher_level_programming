#!/usr/bin/python3
"""
prints UTF8 to STDOUT
"""


def read_file(filename=""):
    """
    opens and reads
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print("{}".format(line.strip(), end=""))
