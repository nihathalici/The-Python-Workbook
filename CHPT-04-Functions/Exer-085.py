"""
Exercise 85: Compute the Hypotenuse

Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
theorem, as the function’s result. Include a main program that reads the lengths of
the shorter sides of a right triangle from the user, uses your function to compute the
length of the hypotenuse, and displays the result.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

import math

def find_hypo(l1, l2):
    h = math.sqrt(l1 ** 2 + l2 ** 2)
    return h

def main():
    side1 = float(input('Enter length of side 1: '))
    side2 = float(input('Enter length of side 2: '))

    hypotenuse = find_hypo(side1, side2)
    print('The hypotenuse of a right triangle with sides %.1f and %.1f is %.1f' % (side1, side2, hypotenuse))

if __name__ == '__main__':
    main()


