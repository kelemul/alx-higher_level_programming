#!/usr/bin/python3
# 12-fizzbuzz.py
# Kelemu L.


def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.
    print fiz for multiples of 3.
    print buzz for multiples of 5
    FizzBuzz for both.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
