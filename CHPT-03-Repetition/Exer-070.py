"""
Exercise 70: Parity Bits

A parity bit is a simple mechanism for detecting errors in data transmitted over an
unreliable connection such as a telephone line. The basic idea is that an additional bit
is transmitted after each group of 8 bits so that a single bit error in the transmission
can be detected.
Parity bits can be computed for either even parity or odd parity. If even parity
is selected then the parity bit that is transmitted is chosen so that the total number
of one bits transmitted (8 bits of data plus the parity bit) is even. When odd parity
is selected the parity bit is chosen so that the total number of one bits transmitted
is odd.
Write a program that computes the parity bit for groups of 8 bits entered by the
user using even parity. Your program should read strings containing 8 bits until the
user enters a blank line. After each string is entered by the user your program should
display a clear message indicating whether the parity bit should be 0 or 1. Display
an appropriate error message if the user enters something other than 8 bits.

Hint: You should read the input from the user as a string. Then you can use
the count method to help you determine the number of zeros and ones in the
string. Information about the count method is available online.
"""
# Author's solution:
##
# Compute the parity bit using even parity for sets of 8 bits entered by the user.
#
# Read the first line of input
line = input("Enter 8 bits: ")

# Continue looping until a blank line is entered
while line != "":
    # Ensure that the line has a total of 8 zeros and ones and exactly 8 characters
    if line.count("0") + line.count("1") != 8 or len(line) != 8:
        # Display an appropriate error message
        print("That wasn’t 8 bits... Try again.")
    else:
        # Count the number of ones
        ones = line.count("1")
        # Display the parity bit
        if ones % 2 == 0:
            print("The parity bit should be 0.")
        else:
            print("The parity bit should be 1.")
    # Read the next line of input
    line = input("Enter 8 bits: ")