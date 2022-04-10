"""
Exercise 74: Square Root

Write a program that implements Newton’s method to compute and display the
square root of a number, x, entered by the user. The algorithm for Newton’s method
follows:
Read x from the user
Initialize guess to x/2
While guess is not good enough do
Update guess to be the average of guess and x/guess

When this algorithm completes, guess contains an approximation of the square
root of x. The quality of the approximation depends on how you define “good
enough”. In the author’s solution, guess was considered good enough when the
absolute value of the difference between guess ∗ guess and x was less than or equal
to 10 ** -12 .
"""

# Solution by Aldo Telese
# https://github.com/aldotele
"""
from math import sqrt

x = float(input('enter x: '))
square_root = sqrt(x)
print('square root of %.2f is' % (x), square_root)

print('implementation: ')
# the guess is initialized to x / 2 (but it does not really change much)
guess = x / 2

while abs(guess ** 2 - x) > 10 ** -12:
    guess = (guess + x / guess) / 2
    print(guess)

print(guess, '--> correct square root')

# note: using equality between guess and square_root as condition would lead to risk of infinite loop
"""

from math import sqrt

x = float(input("Enter x: "))
square_root = sqrt(x)
print('Square root of %.2f is' % (x), square_root)

print('Implementation: ')
# The guess is initialized to x / 2 (but it does not really change much)
guess = x / 2

while abs(guess ** 2 - x) > 10 ** -12:
    guess = (guess + x / guess) / 2
    print(guess)

print(guess, '--> correct square root')
# Aldo Telese's note: 
# Using equality between guess and square_root as condition would lead to risk of infinite loop














