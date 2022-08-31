#!/usr/bin/python3
# 2-uniq_add.py
# Kelemu L.


def uniq_add(my_list=[]):
    """return all unique elements in the list."""
    result = 0
    for x in set(my_list):
        result += x
    return (result)
