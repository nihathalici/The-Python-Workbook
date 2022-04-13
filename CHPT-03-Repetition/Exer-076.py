"""
Exercise 76: Multiple Word Palindromes

There are numerous phrases that are palindromes when spacing is ignored. Examples
include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
among many others. Extend your solution to Exercise 75 so that it ignores spacing
while determining whether or not a string is a palindrome. For an additional challenge,
further extend your solution so that is also ignores punctuation marks and treats
uppercase and lowercase letters as equivalent.
"""

sentence = input('Enter string: ')

# making all lowercase
sentence = sentence.lower()

# it will store only letters without any other type of character
sentence_no_space = ''

for i in range(len(sentence)):
    if 97 <= ord(sentence[i]) <= 122:
        # adding only letters to variable
        sentence_no_space += sentence[i]

print(sentence_no_space)

# here I will create the reverse string in order to compare it with the original
sentence_rev_no_space = ''

j = len(sentence_no_space) - 1

while j > -1:
    sentence_rev_no_space += sentence_no_space[j]
    j -= 1
    
if sentence_rev_no_space == sentence_no_space:
    print('It is a palindrome')
else:
    print('It is not a palindrome')
