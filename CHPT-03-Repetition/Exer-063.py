"""
Exercise 63: Average

In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0.

Hint: Because the 0 marks the end of the input it should not be included in the
average.
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

sum = 0
n = 0

interrupted = False
while not interrupted:
    val = int(input("Enter a value (0 to exit): "))
    if val != 0:
        sum += val
        n += 1
    else:
        interrupted = True

avg = sum / n
print("The average is {].".format(avg))
