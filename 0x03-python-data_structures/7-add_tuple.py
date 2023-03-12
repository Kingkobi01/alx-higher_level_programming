#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = clean_tuple(tuple_a)
    tuple_b = clean_tuple(tuple_b)

    sum_first = tuple_a[0] + tuple_b[0]
    sum_last = tuple_a[1] + tuple_b[1]

    return (sum_first, sum_last)


def clean_tuple(tple=()):
    return tple[:2] + (0, 0) if len(tple) < 2 else tple[:2]
