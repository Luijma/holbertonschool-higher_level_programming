#!/usr/bin/pyton3
def uppercase(str):
    for i in str:
        x = ord(i)
        if x > 96 and x < 123:
            x -= 32
        print(chr(x), end='')
    print('')
