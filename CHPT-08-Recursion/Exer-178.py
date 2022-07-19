"""
Exercise 178: Recursive Palindrome

The notion of a palindrome was introduced previously in Exercise 75. In this exercise
you will write a recursive function that determines whether or not a string is a
palindrome. The empty string is a palindrome, as is any string containing only one
character. Any longer string is a palindrome if its first and last characters match, and
if the string formed by removing the first and last characters is also a palindrome.

Write a main program that reads a string from the user and uses your recursive
function to determine whether or not it is a palindrome. Then your program should
display an appropriate message for the user.
"""

#Author's solution:
##
# Determine whether or not a string entered by the user is a palindrome using recursion.
#
## Determine whether or not a string is a palindrome
# @param s the string to check
# @return True if the string is a palindrome, False otherwise

def isPalindrome(s):
    # Base case: The empty string is a palindrome, False otherwise
    if len(s) <= 1:
        return True

    # Recursive case: The string is a palindrome only
    # if the first and last characters match, and
    # the rest of the string is a palindrome
    return s[0] == s[len(s) - 1] and \
           isPalindrome(s[1 : len(s) - 1])

# Check whether or not a string entered by the user is a palindrome
def main():
    # Read the string from the user
    line = input("Enter a string: ")

    # Check its status and display the result
    if isPalindrome(line):
        print("That was a palindrome!")
    else:
        print("That is not a palindrome.")

# Call the main function
main()
        
        
    
    
    
