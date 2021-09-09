#!/usr/bin/pyton3
def uppercase(str):
    x = ''
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            x += chr(ord(i) -32)
        else:
            x += i
    print("{}".format(x))
