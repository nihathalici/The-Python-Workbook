"""
Exercise 171: Consistent Line Lengths

While 80 characters is a common width for a terminal window, some terminals are
narrow or wider. This can present challenges when displaying documents containing
paragraphs of text. The lines might be too long and wrap, making them difficult to
read, or they might be too short and fail to make good use of the available space.
Write a program that opens a file and displays it so that each line is as full as
possible.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

from pathlib import Path

data_folder = Path("files")
fname = input('Enter a file name to open: ')

try:
    inf = open(data_folder / fname, 'r')
except:
    print('Error, file not found')
    quit()

list_of_lines = inf.readlines()

unique_line = ''.join(list_of_lines)
unique_line = unique_line.replace('\n', ' ')
print('HERE IS THE ORIGINAL BOOK')
print(unique_line)
print()

MAXLEN = int(input('Enter a line\'s max length: '))
print('HERE IS THE FORMATTED BOOK: ')

list_of_words = unique_line.split()
first_word = list_of_words[0]
current_line = first_word

for word in list_of_words[1:]:
    # starting from word two
    # if the length of (current line + word) stays within the limit,
    # I add the word to the current line
    if len(current_line + ' ' + word) <= MAXLEN:
        current_line = current_line + ' ' + word
    
    # otherwise, I print the current line and start a new (current) line
    # where the current word will appear first
    else:
        print(current_line)
        current_line = word
    
    # in case the last word was not included in a previous (already-created) line
    # it means it was added to a new not-printed line
    # if that is the case, I print the last line with the last word
    if current_line and word == list_of_words[-1]:
        print(current_line)

inf.close()
