"""
Exercise 168: Repeated Words

Spelling mistakes are only one of many different kinds of errors that might appear in
a written work. Another error that is common for some writers is a repeated word. For
example, an author might inadvertently duplicate a word, as shown in the following
sentence:

   At least one value must be entered
   entered in order to compute the average.

Some word processors will detect this error and identify it when a spelling or grammar
check is performed.

In this exercise you will write a program that detects repeated words in a text file.
When a repeated word is found your program should display a message that contains
the line number and the repeated word. Ensure that your program correctly handles
the case where the same word appears at the end of one line and the beginning of the
following line, as shown in the previous example. The name of the file to examine will
be provided as the program’s only command line argument. Display an appropriate
error message if the user fails to provide a command line argument, or if an error
occurs while processing the file.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

from words_in_string import words_in_string
import sys
from pathlib import Path

def findDuplicates(myfile):
   duplicates = []
   try:
      inf = open(myfile, 'r')
      # saving each "previous" word in a variable
      # I manage to analyse duplicates between continuous lines by using the variable outside both loops
      last_word = ''

      # looping each line of the file ignoring potential spaces to right and left
      for line in inf:
         line = line.strip()

         # looping each word inside the line/string ignoring punctuation and case through the imported function
         for word in words_in_string(line):
            # in case the current word, edited, is equal to the previous, that is a duplicate
            if word == last_word:
               duplicates.append(word)
            # independently from condition I will always save each looped word in the variable
            last_word = word
      return duplicates

   # showing a customised error only in case the file name is wrong
   except FileNotFoundError:
      return 'Error: File not found'


def main():
   # using the above function but passing the argument (file to read) from CLI
   if len(sys.argv) != 2:
      print('Error: Please provide two arguments')
      quit()
   
   data_folder = Path(".")

   print("Here is the list of duplicates:")
   print(findDuplicates(data_folder / sys.argv[1]))

if __name__ == '__main__':
   main()

""" aldotele's note:
initially did not manage to count duplicates between end of line and start of the next line.
The problem was adding the empty last_word variable inside the first loop. Doing so, when analysing
a new line, the variable was empty again. 
Placing the variable outside both loops, the program always manages to store the previous word
and compare it with the next encountered word.
"""