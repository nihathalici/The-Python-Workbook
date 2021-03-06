"""
Exercise 162: A Book with No E...

The novel “Gadsby” is over 50,000 words in length. While 50,000 words is not
normally remarkable for a novel, it is in this case because none of the words in the
book use the letter E. This is particularly noteworthy when one considers that E is
the most common letter in English.
Write a program that reads a list of words from a file and determines what propor-
tion of the words use each letter of the alphabet. Display this result for all 26 letters
and include an additional message that identifies the letter that is used in the smallest
proportion of the words. Your program should ignore any punctuation marks that are
present in the file and it should treat uppercase and lowercase letters as equivalent.
"""

# Solution by Aldo Telese
# https://github.com/aldotele


from words_in_string import words_in_string
from pathlib import Path

data_folder = Path("files")
filename = input('Enter a file to open: ')
inf = open(data_folder / filename, 'r')
words = []

for line in inf:
    line = line.strip()
    words += words_in_string(line)

# until here I have a list of all the words from the file.txt

words_tot_num = len(words)

# pushing in a list all letters from a to z
letters = []
for i in range(97, 123):
    letters.append(chr(i))

proportions = []
counters = []

for letter in letters:
    counter = 0
    for word in words:
        if letter in word.lower():
            counter += 1
    proportion = (counter / words_tot_num) * 100
    proportions.append('%.1f %%' % proportion)

# until here I will have two lists: a list of letters and a list of proportions
# what I can do is creating a dictionary key-value where I map letters to proportions
# to do it I use zip()

d = dict(zip(letters, proportions))
# printing letters and proportions
# note: the proportions give info about the percentage of words that contain a given letter
for k in d:
    print(k, '>>>', d[k])

# finding the letter with the lowest proportion
min_prop = min(proportions)
smallest_prop_letter = letters[proportions.index(min_prop)]
print('The letter with the smallest proportion is:\n%s >>> %s' % (smallest_prop_letter, min_prop))

"""tip:
if I do not ignore the case, I see that proportion of letter 'i' falls down a lot
this is because very often letter i appears in uppercase when used as a word 'I'
"""


