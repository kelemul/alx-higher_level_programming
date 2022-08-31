#!/usr/bin/python3
# 0-square_matrix_simple.py
# Kelemu L.


def square_matrix_simple(matrix=[]):
    """matrix square."""
    return ([list(map(lambda x: x * x, row)) for row in matrix])
