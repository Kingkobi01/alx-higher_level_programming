#!/usr/bin/python3


def print_last_digit(number):
    last_number = 0
    if number < 0:
        last_number = -1 * (number % -10)
        print("{}".format(last_number), end="")
    else:
        last_number = number % 10
        print("{}".format(last_number), end="")

    return last_number
