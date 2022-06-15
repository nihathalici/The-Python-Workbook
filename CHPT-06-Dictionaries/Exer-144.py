"""
Exercise 144: Anagrams Again

The notion of anagrams can be extended to multiple words. For example, “William
Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
spacing are ignored.
Extend your program from Exercise 143 so that it is able to check if two phrases
are anagrams. Your program should ignore capitalization, punctuation marks and
spacing when making the determination.
"""

# Solution by Aldo Telese
# https://github.com/aldotele
# Modified by:
# https://github.com/nihathalici

def histogram(s):
    ignore_list = ['.', ',', ':', ';', '"', '?', '!', ' ', '<<', '>>']
    s = s.upper()
    h = {}

    for c in s:
        # adding to the histograms only characters which are not in ignore list
        if c not in ignore_list:
            if c not in h:
                h[c] = 1
            else:
                h[c] += 1
    return h
        
def main():
    phrase1 = input('Enter the first phrase: ')
    phrase2 = input('Enter the second phrase: ')

    if histogram(phrase1) == histogram(phrase2):
        print('Those words are anagrams')
    else:
        print('Those words are NOT anagrams')

if __name__ == '__main__':
    main()
