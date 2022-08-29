#!/usr/bin/python3
# 5-no_c.py
# Kelemu L.


def no_c(my_string):
    """remove all c in a string."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
