"""
Exercise 103: Random Good Password

Using your solutions to Exercises 100 and 102, write a program that generates a
random good password and displays it. Count and display the number of attempts
that were needed before a good password was generated. Structure your solution so
that it imports the functions you wrote previously and then calls them from a function
named main in the file that you create for this exercise.

"""

# Solution by Aldo Telese
# https://github.com/aldotele
# Modified by nihathalici

from random_pw import randomPassword
from check_pw import checkPassword

def main():
    attempts = 0
    while True:
        mypwd = randomPassword()
        attempts += 1
        print('Attempt number', attempts, '-->', mypwd)
        if checkPassword(mypwd):
            
            return print('A good password has been created after {} attempts!'.format(attempts))

if __name__ == '__main__':
    main()

