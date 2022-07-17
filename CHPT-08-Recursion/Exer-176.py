"""
Exercise 176: The NATO Phonetic Alphabet

A spelling alphabet is a set of words, each of which stands for one of the 26 letters
in the alphabet. While many letters are easily misheard over a low quality or noisy
communication channel, the words used to represent the letters in a spelling alphabet
are generally chosen so that each sounds distinct and is difficult to confuse with any
other. The NATO phonetic alphabet is a widely used spelling alphabet. Each letter
and its associated word is shown in Table 8.1.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

def phonetic_spelling(s):
    """
    :param s: a word or a sentence (string)
    :return: a string which represents a series of words that do the spelling for the passed string
    """
    spelling = ''

    d = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',\
         'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet',\
         'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',\
         'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',\
         'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee',\
         'Z': 'Zulu'}
    
    # BASE CASE
    # when the passed string has become empty, the spelling is done
    if s == '':
        return ''
    
    # RECURSIVE CASE
    # at each recursion, the program checks if the element is inside the dictionary
    # if so, the spelling variable gets new content
    element = s[0].upper()
    if element in d:
        spelling += d[element]
    
    # each recursion takes the previous spelling content and invoke 
    # the function again from the following element
    return spelling + phonetic_spelling(s[1:])


def main():
    word = input('Enter a word to spell: ')
    print(phonetic_spelling(word))

if __name__ == '__main__':
    main()


