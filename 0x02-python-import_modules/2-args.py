#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    strarg = "argument"
    argc = len(sys.argv) - 1
    count = 1
    if argc != 1:
        strarg += "s"
    if argc >= 1:
        strarg += ":"
    else:
        strarg += "."

    print("{:d} {:s}".format(argc, strarg))

    if argc > 0:
        for par in sys.argv[1:]:
            print("{:d}: {:s}".format(count, par))
            count += 1
