"""
Exercise 159: Two Word Random Password

While generating a password by selecting random characters usually creates one that
is relatively secure, it also generally gives a password that is difficult to memorize.
As an alternative, some systems construct a password by taking two English words
and concatenating them. While this password may not be as secure, it is normally
much easier to memorize.
Write a program that reads a file containing a list of words, randomly selects two
of them, and concatenates them to produce a new password. When producing the
password ensure that the total length is between 8 and 10 characters, and that each
word used is at least three letters long. Capitalize each word in the password so that
the user can easily see where one word ends and the next one begins. Finally, your
program should display the password for the user.
"""
# Author's solution:
from random import randrange

WORD_FILE = "words.txt"
words = []
inf = open(WORD_FILE, "r")
for line in inf:
    # Remove the newline character
    line = line.rstrip()

    # Keep words that are between 3 and 7 letters long
    if len(line) >= 3 and len(line) <= 7:
        words.append(line)

# Close the file
inf.close()

# Randomly select the first word for the password. It can be any word.
first = words[randrange(0, len(words))]
first = first.capitalize()

# Keep selecting a second word until we find one that doesn’t make the password too short
# or too long
password = first
while len(password) < 8 or len(password) > 10:
    second = words[randrange(0, len(words))]
    second = second.capitalize()
    password = first + second

# Display the random password
print("The random password is:", password)
