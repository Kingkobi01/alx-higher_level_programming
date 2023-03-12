#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a:
        tuple_a = clean_tuple(tuple_a)
        tuple_b = clean_tuple(tuple_b)

        first = tuple_a[0] + tuple_b[0]
        last = tuple_a[1] + tuple_b[1]

        return (first, last)


def clean_tuple(tple=()):
    return tple[:2] + (0, 0) if len(tple) < 2 else tple[:2]
