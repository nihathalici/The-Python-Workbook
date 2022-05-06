"""

Exercise 98: Is a Number Prime?

A prime number is an integer greater than one that is only divisible by one and itself.
Write a function that determines whether or not its parameter is prime, returning
True if it is, and False otherwise. Write a main program that reads an integer
from the user and displays a message indicating whether or not it is prime. Ensure
that the main program will not run if the file containing your solution is imported
into another program.

"""
# Author's solution:

##
# Determine if a number entered by the user is prime.
#
## Determine whether or not a number is prime
# @param n the integer to test
# @return True if the number is prime, False otherwise
def isPrime(n):
    if n <= 1:
        return False

    # Check each number from 2 up to but not including n to see if it divides evenly into n
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Determine if a number entered by the user is prime
def main():
    value = int(input("Enter an integer: "))
    if isPrime(value):
        print(value, "is prime.")
    else:
        print(value, "is not prime.")

# Call the main function if the file has not been imported
if __name__ == "__main__":
    main()
    
