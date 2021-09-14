#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]

    if operator == "+":
        result = add(int(argv[1]), int(argv[1]))
    elif operator == "-":
        result = sub(int(argv[1]), int(argv[3]))
    elif operator == "*":
        result = mul(int(argv[1]), int(argv[3]))
    elif operator == "/":
        result = div(int(argv[1]), int(argv[3]))
    else:
        print("Unknown opertor. Available operators: +, -, * and /")
        exit(1)

    print("{:s} {:s} {:s} = {:d}".format(argv[1], operator, argv[3], result))
