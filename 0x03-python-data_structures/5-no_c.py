#!/usr/bin/python3
def no_c(my_string):
    noC = ""
    for current in my_string:
        if current != "C" and current != "c":
            current = current + my_string
    return noC
