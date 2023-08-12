#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        print((((number % 10) * -1) % 10) * -1)

    elif number >= 0:
        print(number%10)
