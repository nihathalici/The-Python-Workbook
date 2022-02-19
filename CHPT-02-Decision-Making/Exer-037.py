"""
Exercise 37: Vowel or Consonant

In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.
"""

vowels = ['a', 'e', 'i', 'o', 'u']

letter = input("Enter a letter: ").lower()

if letter in vowels:
    print("Entered letter is a vowel.")
elif letter == 'y':
    print("Y is sometimes a vowel, and sometimes a consonant.")
else:
    print("The letter is a consonant.")


"""
Author's solution:

letter = input("Enter a letter: ")
if letter == "a" or letter == "e" or \
letter == "i" or letter == "o" or \
letter == "u":
    print("It’s a vowel.")
elif letter == "y":
    print("Sometimes it’s a vowel... Sometimes it’s a consonant.")
else:
    print("It’s a consonant.")
"""

