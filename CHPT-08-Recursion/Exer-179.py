"""
Exercise 179: Recursive Square Root

Exercise 74 explored how iteration can be used to compute the square root of a
number. In that exercise a better approximation of the square root was generated with
each additional loop iteration. In this exercise you will use the same approximation
strategy, but you will use recursion instead of a loop.

Create a square root function with two parameters. The first parameter, n, will
be the number for which the square root is being computed. The second parameter,
guess, will be the current guess for the square root. The guess parameter should have
a default value of 1.0. Do not provide a default value for the first parameter.

Write a main program that demonstrate your square root function by computing
the square root of several different values. When you call your square root function
from the main program you should only pass one parameter to it so that the default
value is used for guess.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

from math import sqrt

def square_root(n, guess=1.0):
    if 10**-12 >= abs(guess**2 - n):
        return guess
    else:
        guess = (guess + n / guess) / 2
        return square_root(n, guess)

def main():
    number = float(input('Enter a number: '))
    print('Its official square root is', sqrt(number))
    print('My estimated square root is', square_root(number, number / 2))

if __name__ == '__main__':
    main()

# note: the first condition in the function is the same as abs(guess**2 - n) <= 10**-12
