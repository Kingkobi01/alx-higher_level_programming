#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if my_list:
        my_list_cp = my_list[:]
        if idx < 0 or idx > (len(my_list_cp) - 1):
            return my_list_cp
        my_list_cp[idx] = element
        return my_list_cp
