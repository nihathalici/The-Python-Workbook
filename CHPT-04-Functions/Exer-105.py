"""
Exercise 105: Arbitrary Base Conversions

Write a program that allows the user to convert a number from one base to another.
Your program should support bases between 2 and 16 for both the input number and
the result number. If the user chooses a base outside of this range then an appropriate
error message should be displayed and the program should exit. Divide your program
into several functions, including a function that converts from an arbitrary base to
base 10, a function that converts from base 10 to an arbitrary base, and a main
program that reads the bases and input number from the user. You may find your
solutions to Exercises 81, 82 and 104 helpful when completing this exercise.
"""

# Author's solution:
##
# Convert a number from one base to another. Both the source base and the destination base
# must be between 2 and 16.
#
from hex_digit import *
## Convert a number from base 10 to base new base
# @param num the base 10 number to convert
# @param new base the base to convert to
# @return the string of digits in new base
def dec2n(num, new_base):
    # Generate the representation of num in base new base, storing it in result
    result = ""
    q = num

    # Perform the body of the loop once
    r = q % new_base
    result = int2hex(r) + result
    q = q // new_base

    # Continue looping until q is 0
    while q > 0:
        r = q % new_base
        result = int2hex(r) + result
        q = q // new_base

    # Return the result
    return result

## Convert a number from base b to base 10
# @param num the base b number, stored in a string
# @param b the base of the number to convert
# @return the base 10 number

def n2dec(num, b):
    decimal = 0

    # Process each digit in the base b number
    for i in range(len(num)):
        decimal = decimal * b
        decimal = decimal + hex2int(num[i])

    # Return the result
    return decimal

# Convert a number between two arbitrary bases
def main():
    # Read the base and number from the user
    from_base = int(input("Base to convert from (2-16): "))
    if from_base < 2 or from_base > 16:
        print("Only bases between 2 and 16 are supported.")
        print("Quitting...")
        quit()
    
    from_num = input("Sequence of digits in that base: ")

    # Convert to base 10 and display the result
    dec = n2dec(from_num, from_base)
    print("That's %d in base 10." % dec)

    # Convert to the new base and display the result
    to_base = int(input("Enter the base to convert to (2-16): "))
    if to_base < 2 or to_base > 16:
        print("Only bases between 2 and 16 are supported.")
        print("Quitting...")
        quit()
    
    to_num = dec2n(dec, to_base)
    print("That's %s in base %d." % (to_num, to_base))

# Call the main function
main()


    
