"""
Exercise 167: Spell Checker

A spell checker can be a helpful tool for people who struggle to spell words correctly.
In this exercise, you will write a program that reads a file and displays all of the words
in it that are misspelled. Misspelled words will be identified by checking each word
in the file against a list of known words. Any words in the user’s file that do not
appear in the list of known words will be reported as spelling mistakes.
"""

from words_in_string import words_in_string
import sys
from pathlib import Path

def check_misspelled(myfile, base_file):
    misspelled = []
    # reading a base file containing all possible words
    # from that file I create a dictionary where each key is a word
    all_words_file = open(base_file, 'r')
    all_words_d = dict()
    for line in all_words_file:
        line = line.strip()
        all_words_d[line] = 0
    
    all_words_file.close()

    # reading the file upon which I have to make the check
    # looping each word of the file ignoring punctuation and case
    # if the single looped word is not present in the base dictionary, then is a misspelled
    # pushing the misspelled in the output list, only if not already present
    myf = open(myfile, 'r')
    for line in myf:
        for word in words_in_string(line):
            if word.lower() not in all_words_d and not word.isdigit():
                if word.lower() not in misspelled:
                    misspelled.append(word)
    myf.close()

    return misspelled

def main():
    data_folder = Path('files')
    if len(sys.argv) != 3:
        print('Please insert three parameters in command line')
        quit()
    
    # passing through CLI the files upon which to make the comparison
    # after the script, the first passed file will be the one to check, while the latter contains all words
    try:
        for word in check_misspelled(data_folder / sys.argv[1], data_folder / sys.argv[2]):
            print(word, end='  ')
    
    except:
        print('Something went wrong: try checking the name of the files')

if __name__ == '__main__':
    main()



