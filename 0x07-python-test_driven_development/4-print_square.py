""" Print Square Module """


def print_square(size):
    """ prints a square with given size """

    if (type(size) != int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    if (size != 0):
        for j in range(0, size):
            for i in range(0, size):
                print("#", end="")
            print("")
    else:
        print("")
