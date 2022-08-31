#!/usr/bin/python3
# 9-multiple_by_2.py
# kelmeu L.


def multiply_by_2(a_dictionary):
    """multiply a dict by 2."""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
