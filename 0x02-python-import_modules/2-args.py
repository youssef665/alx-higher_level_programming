#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    count = len(argv) - 1

    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:\n1: {}".format(count, argv[count]))
    else:
        print("{} arguments:".format(count))

        for i in range(count):
            print("{}: {}".format(i + 1, argv[i + 1]))
