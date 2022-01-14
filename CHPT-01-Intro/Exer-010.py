"""
Exercise 10: Arithmetic

Create a program that reads two integers, a and b, from the user. Your program should
compute and display:

The sum of a and b
The difference when b is subtracted from a
The product of a and b
The quotient when a is divided by b
The remainder when a is divided by b
The result of log 10 a
The result of a b

Hint: You will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""
import math

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print()
print("The sum of a and b: {}".format(a+b))
print("The difference when b is subtracted from a: {}".format(a-b))
print("The product of a and b: {}".format(a*b))
print("The quotient when a is divided by b: {}".format(a/b))
print("The remainder when a is divided by b: {}".format(a%b))
print("The result of log 10 a: {}".format(math.log10(a)))
print("The result of a ˆ b: {}".format(math.pow(a, b)))

"""
Author's solution:

from math import log10

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print(a, "+", b, "is", a + b)
print(a, "-", b, "is", a - b)
print(a, "*", b, "is", a * b)
print(a, "/", b, "is", a / b)
print(a, "%", b, "is", a % b)

print("The base 10 logarithm of", a, "is", log10(a))
print(a, "ˆ", b, "is", a**b)
"""
