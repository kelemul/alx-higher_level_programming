#!/usr/bin/python3
# 11-multiply_list_map.py
# kelemu L.


def multiply_list_map(my_list=[], number=0):
    """ Returns a list multiplied by a number."""
    return (list(map(lambda x: x*number, my_list)))
