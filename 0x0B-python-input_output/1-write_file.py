#!/usr/bin/python3
"""
writes
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file
    """

    count = 0
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)
        return len(text)
