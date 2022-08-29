#!/usr/bin/python3
# 8-multiple_returns.py
# Kelemu L.


def multiple_returns(sentence):
    """return sentence lenght."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
