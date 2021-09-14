#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    argc = len(sys.argv)

    if argc != 1:
        for i in sys.argv[1:]:
            count += int(i)

    print("{:d}".format(count))
