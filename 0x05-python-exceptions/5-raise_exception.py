#!/usr/bin/python3
def raise_exception():
    try:
        num = 1 + "enock"
    except Exception as e:
        raise (TypeError)

