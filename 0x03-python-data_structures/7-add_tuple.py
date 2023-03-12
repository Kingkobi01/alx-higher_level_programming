#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a:
        tuple_a = clean_tuple(tuple_a)
        tuple_b = clean_tuple(tuple_b)

        first = tuple_a[0] + tuple_b[0]
        last = tuple_a[1] + tuple_b[1]

        return (first, last)


def clean_tuple(tple=()):
    if len(tple) < 2:
        if len(tple) == 1:
            tple = (tple[0], 0)
        else:
            tple = (0, 0)
    elif len(tple) > 2:
        tple = (tple[0], tple[1])

    return tple
