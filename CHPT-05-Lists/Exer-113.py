"""
Exercise 113: Avoiding Duplicates

In this exercise, you will create a program that reads words from the user until the
user enters a blank line. After the user enters a blank line your program should dis-
play each word entered by the user exactly once. The words should be displayed in
the same order that they were first entered. For example, if the user enters:

first
second
first
third
second

then your program should display:

first
second
third

"""
# Author's solution:
##
# Read a collection of words entered by the user. Display each word
# entered by the user only once, in the same order
# that the words were entered.
#
# Read words from the user and store them in a list
words = []
word = input("Enter a word (blank line to quit): ")
while word != "":
    # Only add the word to the list if
    # it is not already present in it
    if word not in words:
        words.append(word)

    # Read the next word from the user
    word = input("Enter a word (blank line to quit): ")

for word in words:
    print(word)
