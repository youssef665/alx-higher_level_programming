#!/usr/bin/python3

from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        n = add(a, b)
        for i in range(4, 6):
            n = add(n, i)
        return (n)
    else:
        return(sub(a, b))

