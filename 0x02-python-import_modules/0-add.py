#!/usr/bin/python3
# 0_add.py
# Kelemu L.

if __name__ == "__main__":
    """import add() from add_0 and sum the arguments"""
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
