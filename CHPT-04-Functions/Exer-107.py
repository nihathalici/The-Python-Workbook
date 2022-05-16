"""
Exercise 107: Reduce a Fraction to Lowest Terms

Write a function that takes two positive integers that represent the numerator and
denominator of a fraction as its only parameters. The body of the function should
reduce the fraction to lowest terms and then return both the numerator and denominator
of the reduced fraction as its result. For example, if the parameters passed
to the function are 6 and 63 then the function should return 2 and 21. Include a
main program that allows the user to enter a numerator and denominator. Then your
program should display the reduced fraction.

Hint: In Exercise 79 you wrote a program for computing the greatest common
divisor of two positive integers. You may find that code useful when completing
this exercise.
"""

# Author's solution:
##
# Reduce a fraction to lowest terms.
#
## Compute the greatest common divisor of two integers
# @param n the first integer under consideration (must be non-zero)
# @param m the second integer under consideration (must be non-zero)
# @return the greatest common divisor of the integers

def gcd(n, m):
    # Initialize d to the smaller of n and m
    d = min(n, m)
    # Use a while loop to find the greatest common divisor of n and m
    while n % d != 0 or m % d != 0:
        d = d - 1
    return d

## Reduce a fraction to lowest terms
# @param num the integer numerator of the fraction
# @param den the integer denominator of the fraction (must be non-zero)
# @return the numerator and denominator of the reduced fraction
def reduce(num, den):
    # If the numerator is 0 then the reduced fraction is 0 / 1
    if num == 0:
        return (0, 1)
    
    # Compute the greatest common divisor of the numerator and denominator
    g = gcd(num, den)

    # Divide both the numerator and denominator by the GCD and return the result
    return (num // g, den // g)

# Read a fraction from the user and display the equivalent lowest terms fraction
def main():
    # Read the numerator and denominator from the user
    num = int(input("Enter the numerator: "))
    den = int(input("Enter the denominator: "))

    # Compute the reduced fraction
    (n, d) = reduce(num, den)

    # Display the result
    print("%d/%d can be reduced to %d/%d." % (num, den, n, d))

# Call the main function
main()






