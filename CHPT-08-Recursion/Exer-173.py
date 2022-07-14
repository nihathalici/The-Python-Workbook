"""
Exercise 173: Total the Values

Write a program that reads values from the user until a blank line is entered. Display
the total of all of the values entered by the user (or 0.0 if the first value entered is
a blank line). Complete this task using recursion. Your program may not use any
loops.

Hint: The body of your recursive function will need to read one value from the
user, and then determine whether or not to make a recursive call. Your function
does not need to take any arguments, but it will need to return a numeric result.
"""


# Author's solution:
##
# Total a collection of numbers entered by the user. The user will enter a blank line to
# indicate that no further numbers will be entered and the total should be displayed.
#
## Total all of the numbers entered by the user until the user enters a blank line
# @return the total of the entered values
def readAndTotal():
    # Read a value from the user
    line = input("Enter a number (blank to quit): ")

    # Base case: The user entered a blank line so the total is 0
    if line == "":
        return 0
    else:
        # Recursive case: Convert the current line to a number and use recursion to read the
        # subsequent lines
        return float(line) + readAndTotal()

# Read a collection of numbers from the user and display the total
def main():
    # Read the values from the user and compute the total
    total = readAndTotal()

    # Display the total
    print("The total of all those values is", total)

main()
