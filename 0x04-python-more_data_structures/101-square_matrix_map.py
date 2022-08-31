#!/usr/bin/python3
# 101-square_matrix_map.py
# Kelmeu L.


def square_matrix_map(matrix=[]):
    """ returns the square of the matrix"""
    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))
