"""
Exercise 75: Is a String a Palindrome?

A string is a palindrome if it is identical forward and backward. For example “anna”,
“civic”, “level” and “hannah” are all examples of palindromic words. Write a program
that reads a string from the user and uses a loop to determine whether or not it is a
palindrome. Display the result, including a meaningful output message.
Aibohphobia is the extreme or irrational fear of palindromes. This word was
constructed by prepending the -phobia suffix with it’s reverse, resulting in
a palindrome. Ailihphilia is the fondness for or love of palindromes. It was
constructed in the same manner from the -philia suffix.
"""
# Author's solution:
# Modified by nihathalici
##
# Determine whether or not a string entered by the user is a palindrome.
#
# Read the string from the user
inp = input("Enter a string: ")
line = inp.lower()

# Assume that it is a palindrome until we can prove otherwise
is_palindrome = True

# Check the characters, starting from the ends. Continue until the middle is reached or we have
# determined that the string is not a palindrome.
i = 0
while i < len(line) / 2 and is_palindrome:
    # If the characters do not match then mark that the string is not a palindrome
    if line[i] != line[len(line) - i - 1]:
        is_palindrome = False
    # Move to the next character
    i = i + 1

# Display a meaningful output message
if is_palindrome:
    print(inp, "is a palindrome")
else:
    print(inp, "is not a palindrome")


