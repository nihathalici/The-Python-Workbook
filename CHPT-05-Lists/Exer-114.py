"""
Exercise 114: Negatives, Zeros and Positives

Create a program that reads integers from the user until a blank line is entered. Once
all of the integers have been read your program should display all of the negative
numbers, followed by all of the zeros, followed by all of the positive numbers. Within
each group the numbers should be displayed in the same order that they were entered
by the user. For example, if the user enters the values
3, -4, 1, 0, -1, 0, and -2
then your program should output the values
-4, -1, -2, 0, 0, 3, and 1.
Your program should display each value on its own line.
"""
# Author's solution:
##
# Read a collection of integers from the user. Display all of the negative numbers, followed
# by all of the zeros, followed by all of the positive numbers.
#
# Create three lists to store the negative, zero and positive values
negatives = []
zeros = []
positives = []

# Read all of the integers from the user, storing each integer in the correct list
line = input("Enter an integer (blank to quit): ")
while line != "":
    num = int(line)

    if num < 0:
        negatives.append(num)
    elif num > 0:
        positives.append(num)
    else:
        zeros.append(num)

    # Read the next line of input from the user
    line = input("Enter an integer (blank to quit): ")

# Display all of the negative values, then all of the zeros, then all of the positive values
print("The numbers were: ")

for n in negatives:
    print(n)

for n in zeros:
    print(n)

for n in positives:
    print(n)

