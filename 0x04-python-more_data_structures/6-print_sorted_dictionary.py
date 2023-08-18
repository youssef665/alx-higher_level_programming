#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    li = list(a_dictionary.keys())
    li.sort()

    for i in li:

        print("{}: {}".format(i, a_dictionary.get(i)))
