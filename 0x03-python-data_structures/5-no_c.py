#!/usr/bin/python3
def no_c(my_string):
    noC = ""
    for current in my_string:
        if current != "C" and current != "c":
            noC += current
    return noC
