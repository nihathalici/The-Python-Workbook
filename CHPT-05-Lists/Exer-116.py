"""
Exercise 116: Perfect Numbers

An integer, n, is said to be perfect when the sum of all of the proper divisors of n is
equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.

Write a function that determines whether or not a positive integer is perfect. Your
function will take one parameter. If that parameter is a perfect number then your
function will return True. Otherwise it will return False. In addition, write a main
program that uses your function to identify and display all of the perfect numbers
between 1 and 10,000. Import your solution to Exercise 115 when completing this
task.
"""
# Author's solution:
##
# A number, n, is a perfect number if the sum of the proper divisors of n is equal to n. This
# program displays all of the perfect numbers between 1 and LIMIT.
#
from proper_divisors import properDivisors

LIMIT = 10000

## Determine whether or not a number is perfect. A number is perfect if the sum of its proper
# divisors is equal to the number itself.
# @param n the number to check for perfection
# @return True if the number is perfect, False otherwise
def isPerfect(n):
    # Get a list of the proper divisors of n
    divisors = properDivisors(n)

    # Compute the total of all of the divisors
    total = 0
    for d in divisors:
        total += d

    # Determine whether or not the number is perfect
    # and return the appropriate result
    if total == n:
        return True
    return False

# Display all of the perfect numbers between 1 and LIMIT
def main():
    print("The perfect numbers between 1 and", LIMIT, "are:")
    for i in range(1, LIMIT + 1):
        if isPerfect(i):
            print(" ", i)

main()
    
