"""
Exercise 77: Multiplication Table

In this exercise you will create a program that displays a multiplication table that
shows the products of all combinations of integers from 1 times 1 up to and including
10 times 10. Your multiplication table should include a row of labels across the top
of it containing the numbers 1 through 10. It should also include labels down the left
side consisting of the numbers 1 through 10. The expected output from the program
is shown below:


When completing this exercise you will probably find it helpful to be able to
print out a value without moving down to the next line. This can be accomplished
by added end="" as the last argument to your print statement. For example,
print("A") will display the letter A and then move down to the next line. The
statement print("A", end="") will display the letter A without moving down
to the next line, causing the next print statement to display its result on the same line
as the letter A.
"""

# Author's solution:
##
# Display a multiplication table for 1 times 1 through 10 times 10.
#
MIN = 1
MAX = 10

# Display the top row of labels
print("    ", end="")
for i in range(MIN, MAX + 1):
    # Including end="" as the final argument to print
    # prevents it from moving down to
    # the next line after displaying the value.
    print("%4d" % i, end="")
print()

# Display the table
for i in range(MIN, MAX + 1):
    print("%4d" % i, end="")
    for j in range(MIN, MAX + 1):
        print("%4d" % (i * j), end="")
    print()
