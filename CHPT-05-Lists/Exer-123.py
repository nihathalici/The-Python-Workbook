"""
Exercise 123: Pig Latin Improved

Extend your solution to Exercise 122 so that it correctly handles uppercase letters and
punctuation marks such as commas, periods, question marks and exclamation marks.
If an English word begins with an uppercase letter then its Pig Latin representation
should also begin with an uppercase letter and the uppercase letter moved to the end of
the word should be changed to lowercase. For example, Computer should become
Omputercay. If a word ends in a punctuation mark then the punctuation mark
should remain at the end of the word after the transformation has been performed.
For example, Science! should become Iencescay!.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

from string import punctuation


string = input('Enter text: ')
res = ''
vowels = ['a', 'e', 'i', 'o', 'u']
punctuation = [',', '.', '?', '!']
punct = ''

i = len(string) - 1
for c in string:
    while string[i] in punctuation:
        punct += string[i]
        i -= 1

mylength = len(string) - len(punct)

if string[0].lower() in vowels:
    final = 'way'
    res = string + final
else:
    final = ''
    initial = ''
    for i in range(mylength):
        if string[i].lower() not in vowels:
            final += string[i].lower()
        else:
            if string[0].isupper():
                initial = string[i].upper() + string[i+1:mylength]
            else:
                initial = string[i] + string[i+1:mylength]
            break
    res = initial + final + 'ay' + punct

print(res)


