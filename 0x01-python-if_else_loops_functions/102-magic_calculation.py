#!/usr/bin/python3
# 102-magic_calculation.py
# kelemu


def magic_calculation(a, b, c):
    """Match bytecode."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
