"""
Exercise 118: Word by Word Palindromes

Exercises 75 and 76 previously introduced the notion of a palindrome. Such palin-
dromes examined the characters in a string, possibly ignoring spacing and punc-
tuation marks, to see if the string was the same forwards and backwards. While
palindromes are most commonly considered character by character, the notion of
a palindrome can be extended to larger units. For example, while the sentence “Is
it crazy how saying sentences backwards creates backwards sentences saying how
crazy it is?” isn’t a character by character palindrome, it is a palindrome when exam-
ined a word at a time (and when capitalization and punctuation are ignored). Other
examples of word by word palindromes include “Herb the sage eats sage, the herb”
and “Information school graduate seeks graduate school information”.

Create a program that reads a string from the user. Your program should report
whether or not the entered string is a word by word palindrome. Ignore spacing and
punctuation when determining the result.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

import string

def is_wbw_palindrome(sentence):

    s_list = sentence.split()

    for i in range(len(s_list)):
        word = s_list[i].strip(string.punctuation).lower()
        s_list[i] = word

    s_list_rev = []
    rev_index = len(s_list) - 1
    for i in range(len(s_list)):
        s_list_rev.append(s_list[rev_index])
        rev_index -= 1

    if s_list == s_list_rev:
        return True
    else:
        return False

def main():
    mystring = input('Please enter a sentence: ')

    if is_wbw_palindrome(mystring):
        print('That\'s a word by word palindrome')
    else:
        print('Not a word by word palindrome')

if __name__ == '__main__':
    main()
