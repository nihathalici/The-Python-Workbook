"""
Exercise 153: Find the Longest Word in a File

In this exercise you will create a Python program that identifies the longest word(s)
in a file. Your program should output an appropriate message that includes the length
of the longest word, along with all of the words of that length that occurred in the file.
Treat any group of non-white space characters as a word, even if it includes digits or
punctuation marks.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

import os.path

input_file = input('Please enter file name: ')
file_to_open = os.path.join("files", input_file)
fin = open(file_to_open, 'r')

last_length = 0
words = []

for line in fin:
    for el in line.split():
        if len(el) > last_length:
            words = [el]
            last_length = len(el)
        elif len(el) == last_length:
            if el not in words:
                words.append(el)

print('Length of longest word(s): %d' % last_length)
print('Words: %s' % words)
    










