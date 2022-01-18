#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    index = 0
    while(index < x):
       try:
           print("{:d}".format(my_list[index]), end="")
       except ValueError:
           index += 1
       except TypeError:
           index += 1
       else:
           printed += 1
           index += 1
    print("")
    return printed
