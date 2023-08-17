#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    from sys import argv, exit

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    o = {"+": add, "-": sub, "*": mul, "/": div}

    if argv[2] not in list(o.keys()):

        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    x = int(argv[1])
    y = int(argv[3])

    print("{} {} {} = {}".format(x, argv[2], y, o[argv[2]](x, y)))
