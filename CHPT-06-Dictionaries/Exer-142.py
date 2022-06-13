"""
Exercise 142: Unique Characters

Create a program that determines and displays the number of unique characters in a
string entered by the user. For example, Hello, World! has 10 unique characters
while zzz has only one unique character. Use a dictionary or set to solve this problem.
"""
# Author's solution:
##
# Compute the number of unique characters in a string using a dictionary.
#
# Read the string from the user
s = input("Enter a string: ")

# Add each character to a dictionary with a value of True. Once we are done the number
# of keys in the dictionary will be the number of unique characters in the string.
characters = {}
for ch in s:
    characters[ch] = True

print("That string comtained", len(characters), \
      "unique character(s).")
