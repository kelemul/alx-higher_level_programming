#!/usr/bin/python3
# 6-print_sorted_dictionary.py
# kelemu L.


def print_sorted_dictionary(a_dictionary):
    """print in sorted order."""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
