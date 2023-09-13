#!/usr/bin/python3

"""Defines pascal triangle."""


def pascal_triangle(n):
    """Represent pascal triagle of size.

    Returns a list of integers

    """
    if n <= 0:
        return []

    ptriangle = [[1]]

    while len(ptriangle) != n:
        t = ptriangle[-1]
        tm = [1]
        for i in range(len(t) - 1):
            tm.append(t[i] + t[i + 1])
        tm.append(1)

        ptriangle.append(tm)

    return ptriangle
