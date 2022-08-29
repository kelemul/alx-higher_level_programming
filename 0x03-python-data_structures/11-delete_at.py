#!/usr/bin/python3
# 11-delete_at.py
# Kelemu L. 


def delete_at(my_list=[], idx=0):
    """delete at element at index idx."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
