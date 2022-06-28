"""
Exercise 157: Both Letter Grades and Grade Points

Write a program that converts from letter grades to grade points and vice-versa. Your
program should allow the user to convert multiple values, with one value entered on
each line. Begin by attempting to convert each value entered by the user from a
number of grade points to a letter grade. If an exception occurs during this process
then your program should attempt to convert the value from a letter grade to a number
of grade points. If both conversions fail then your program should output a message
indicating that the supplied input is invalid. Design your program so that it continues
performing conversions (or reporting errors) until the user enters a blank line. Your
solutions to Exercises 52 and 53 may be helpful when completing this exercise.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

from lett_to_point import lett_to_point
from point_to_lett import point_to_lett

def grade_converter(value):
    try:
        res = point_to_lett(value)
        return res
    except:
        try:
            res = lett_to_point(value)
            return res
        except:
            raise ValueError('The supplied input is not valid.')


def main():
    mygrade = input('Enter either a letter or point grade: ')
    while mygrade != '':
        try:
            print(grade_converter(mygrade))
            mygrade = input('Enter either a letter or point grade: ')
        except:
            print('Invalid input, retry')
            mygrade = input('enter either a letter or point grade: ')

if __name__ == '__main__':
    main()
