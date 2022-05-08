"""
Exercise 99: Next Prime

In this exercise you will create a function named nextPrime that finds and returns
the first prime number larger than some integer, n. The value of n will be passed to
the function as its only parameter. Include a main program that reads an integer from
the user and displays the first prime number larger than the entered value. Import
and use your solution to Exercise 98 while completing this exercise.

"""

# Solution by Aldo Telese
# https://github.com/aldotele

from is_prime import isPrime

def nextPrime(n):
    i = n + 1
    while True:
        if isPrime(i):
            return i
        i += 1

def main():
    value = int(input('Enter a number: '))
    print('The first prime after {} is {}'.format(value, nextPrime(value)))

if __name__ == '__main__':
    main()

