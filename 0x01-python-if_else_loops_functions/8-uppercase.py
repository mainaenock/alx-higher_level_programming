#!/usir/bin/python3
def uppercase(str):
    sent = ""
    for i in str:
        c = ord(i)
        if ord('a') <= c <= ord('z'):
            sent += (chr(c - 32))
        else:
            sent += (chr(c))
    print("{}".format(sent))
