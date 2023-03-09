#!/usr/bin/python3


def fizzbuzz():
    for i in range(1, 101):
        separator = " " if i < 100 else ""
        if i % 15 == 0:
            print("FizzBuzz", end=separator)
        elif i % 3 == 0:
            print("Fizz", end=separator)
        elif i % 5 == 0:
            print("Buzz", end=separator)
        else:
            print("{}".format(i), end=separator)
