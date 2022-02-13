
"""
Exercise 33: Sort 3 Integers

Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
"""

# Author's solution:

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

mn = min(a, b, c)
mx = max(a, b, c)
md = a + b + c - mn - mx

print("The numbers in sorted order are:\n{}\n{}\n{}".format(mn, md, mx))

