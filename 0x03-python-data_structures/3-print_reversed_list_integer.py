#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    last = (len(my_list) * -1) + -1
    for numb in range(-1, last, -1):
        print("{:d}".format(my_list[numb]))
