#!/usr/bin/python3
def element_at(mylist, idx):
    if idx < 0:
        return None
    elif idx > len(mylist):
        return None
    else:
        return mylist[idx]
