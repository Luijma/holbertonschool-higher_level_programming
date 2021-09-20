#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    idx1s = []
    idx2s = []
    for i in range(2):
        if i < len(tuple_a):
            idx1s.append(tuple_a[i])
        else:
            idx1s.append(0)
    for i in range(2):
        if i < len(tuple_b):
            idx2s.append(tuple_b[i])
        else:
            idx2s.append(0)

    a = idx1s[0] + idx2s[0]
    b = idx1s[1] + idx2s[1]
    new_tuple = (a, b)
    return new_tuple
