#!/usr/bin/python3
# 10-divisible_by_2.py
# Kelemu L.


def divisible_by_2(my_list=[]):
    """get multiples of 2."""
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
