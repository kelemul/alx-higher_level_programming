#!/usr/bin/python3
# 2-replace_in_list.py
# Kelemu L.


def replace_in_list(my_list, idx, element):
    """replace at index idx."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
