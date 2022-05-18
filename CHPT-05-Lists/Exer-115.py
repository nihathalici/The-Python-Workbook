"""
Exercise 115: List of Proper Divisors

A proper divisor of a positive integer, n, is a positive integer less than n which divides
evenly into n. Write a function that computes all of the proper divisors of a positive
integer. The integer will be passed to the function as its only parameter. The function
will return a list containing all of the proper divisors as its only result. Complete
this exercise by writing a main program that demonstrates the function by reading
a value from the user and displaying the list of its proper divisors. Ensure that your
main program only runs when your solution has not been imported into another file.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

def proper_divisors(n):
    list_of_divisors = []
    for i in range(1, n):
        if n % i == 0:
            list_of_divisors.append(i)
    return list_of_divisors

def main():
    number = int(input("Enter integer: "))
    print(proper_divisors(number))

if __name__ == '__main__':
    main()
