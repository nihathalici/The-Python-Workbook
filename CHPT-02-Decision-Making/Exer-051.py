"""
Exercise 51: Roots of a Quadratic Function

A univariate quadratic function has the form f (x) = ax ** 2 + bx + c, where a, b and c
are constants, and a is non-zero. Its roots can be identified by finding the values of x
that satisfy the quadratic equation ax ** 2 + bx + c = 0. These values can be computed
using the quadratic formula, shown below. A quadratic function may have 0, 1 or 2
real roots.

The portion of the expression under the square root sign is called the discriminant.
If the discriminant is negative then the quadratic equation does not have any real
roots. If the discriminant is 0, then the equation has one real root. Otherwise the
equation has two real roots, and the expression must be evaluated twice, once using
a plus sign, and once using a minus sign, when computing the numerator.

Write a program that computes the real roots of a quadratic function. Your pro-
gram should begin by prompting the user for the values of a, b and c. Then it should
display a message indicating the number of real roots, along with the values of the
real roots (if any).
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

print("This program calculates the real roots of a quadratic equation(if any).")
a = float(input("Please enter a value for a: "))
b = float(input("Please enter a value for b: "))
c = float(input("Please enter a value for c: "))

discriminate = b**2 - 4*a*c

if discriminate < 0:
	print("This quadratic function doesn't have any real roots.")
	
elif discriminate == 0:
	print("This quadratic function has one real root.")
	
	root = -b / 2*a 
	
	print("Real root = {}".format(root))
	
elif discriminate > 0:
	print("This quadratic function has two real roots.")
	
	root1 = -b + discriminate / 2*a
	root2 = -b - discriminate / 2*a 
	
	print("Real roots = {} or {}".format(root1, root2))
