#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        maxnum = my_list[0]
        i = 0
        while i < len(my_list):
            if maxnum < my_list[i]:
                maxnum = my_list[i]
            i += 1
        return maxnum
    else:
        return None
