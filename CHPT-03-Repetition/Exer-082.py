"""
Exercise 82: Decimal to Binary

Write a program that converts a decimal (base 10) number to binary (base 2). Read the
decimal number from the user as an integer and then use the division algorithm shown
below to perform the conversion. When the algorithm completes, result contains the
binary representation of the number. Display the result, along with an appropriate
message.

Let result be an empty string
Let q represent the number to convert

repeat
  Set r equal to the remainder when q is divided by 2
  Convert r to a string and add it to the beginning of result
  Divide q by 2, discarding any remainder, and store the result back into q
until q is 0
"""
# Author's solution
##
# Convert a number from decimal (base 10) to binary (base 2).
#
NEW_BASE = 2

# Read the number to convert from the user
num = int(input("Enter a non-negative integer: "))

# Generate the binary representation of num, storing it in result
result = ""
q = num

# Perform the body of the loop once
r = q % NEW_BASE
result = str(r) + result
q = q // NEW_BASE

# Keep on looping until q is 0
while q > 0:
    r = q % NEW_BASE
    result = str(r) + result
    q = q // NEW_BASE

# Display the result
print(num, "in decimal is", result, "in binary.")
    
