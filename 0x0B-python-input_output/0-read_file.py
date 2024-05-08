#!/usr/bin/python3
"""
prints UTF8 to STDOUT
"""


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        opened = file.read()
        print("{}".format(opened))
