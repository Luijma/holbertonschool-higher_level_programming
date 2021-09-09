#!/usr/bin/pyton3
def uppercase(str):
    capword = str
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            capword = capword.replace(i, chr(ord(i) - 32))
    print(capword)
