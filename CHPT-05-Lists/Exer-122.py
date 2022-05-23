"""
Exercise 122: Pig Latin

Pig Latin is a language constructed by transforming English words. While the ori-
gins of the language are unknown, it is mentioned in at least two documents from
the nineteenth century, suggesting that it has existed for more than 100 years. The
following rules are used to translate English into Pig Latin:

If the word begins with a consonant (including y), then all letters at the beginning of
the word, up to the first vowel (excluding y), are removed and then added to the end
of the word, followed by ay. For example, computer becomes omputercay
and think becomes inkthay.

If the word begins with a vowel (not including y), then way is added to the end
of the word. For example, algorithm becomes algorithmway and office
becomes officeway.

Write a program that reads a line of text from the user. Then your program should
translate the line into Pig Latin and display the result. You may assume that the string
entered by the user only contains lowercase letters and spaces.
"""

string = input('Enter text: ')
res = ''
vowels = ['a', 'e', 'i', 'o', 'u']

if string[0] in vowels:
    final = 'way'
    res = string + final
else:
    final = ''
    initial = ''

    for i in range(len(string) -1):

        if string[i] not in vowels:
            final += string[i]
        else:
            initial += string[i:]
            break
    res = initial + final + 'ay'

print(res)