"""
Exercise 160: Weird Words

Students learning to spell in English are often taught the rhyme “I before E except
after C”. This rule of thumb advises that when an I and an E are adjacent in a word,
the I will precede the E, unless they are immediately preceded by a C. When preceded
by a C the E will appear ahead of the I. This advice holds true for words without an
immediately preceding C such as believe, chief, fierce and friend, and is similarly
true for words with an immediately preceding C such as ceiling and receipt. However,
there are exceptions to this rule, such as weird.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

import string

def contains_adjacent_e_i(word):
    """
    :param word: string
    :return: True if the word contains adjacent 'e' and 'i' (e.g. ceiling, scientist, etc.), False otherwise
    """
    if 'e' in word and 'i' in word:
        for i in range(len(word)):
            if i != len(word) - 1:
                if (word[i] == 'e' and word[i+1] == 'i' or word[i] == 'i' and word[i+1] == 'e'):
                    return True
    return False

def rhyme_rule(word):
    """
    it applies the <<I before E except after C>> rule
    :param word: a string
    :return: True if the word respects the rule, False otherwise
    """
    word = word.lower()
    if 'e' in word and 'i' in word:
        for i in range(len(word)):
            if word[i] == 'c' and word[i+1] == 'i' and word[i+2] == 'e':
                return False
            elif i != 0 and i != len(word)-1:
                if word[i] == 'e' and word[i+1] == 'i' and word[i-1] != 'c':
                    return False
    return True
    


def main():
    inf = open('emma.txt', 'r')
    respecting = []
    not_respecting = []
    for line in inf:
        line = line.strip()
        for word in line.split():
            # removing punctuations to left and right of the word in order to count the same words only once
            word = word.strip(string.punctuation)
            # if the word contains adjacent 'e' and 'i', it gets analyzed
            if contains_adjacent_e_i(word):
                # if the word respects the rule, it gets added to the list of respecting words (if not present)
                if rhyme_rule(word):
                    if word.lower() not in respecting:
                        respecting.append(word)
                # otherwise, if not already added before, the not respecting word gets added to the other list
                else:
                    if word not in not_respecting:
                        not_respecting.append(word)

    print('Words that respect the rule: {}'.format(len(respecting)))
    print(respecting)
    print('Words that do not respect the rule: {}'.format(len(not_respecting)))
    print(not_respecting)

    tot_adjacent_ei_words = len(respecting) + len(not_respecting)
    respecting_proportion = len(respecting) / tot_adjacent_ei_words
    not_respecting_proportion = len(not_respecting) / tot_adjacent_ei_words
    print()
    print("In total, {} words that include adjacent 'e' and 'i' were found".format(tot_adjacent_ei_words))
    print("Among them, %.2f %% respect the rule and %.2f %% do not respect the rule"\
        % (respecting_proportion * 100, not_respecting_proportion * 100))
    
    inf.close()

if __name__ == '__main__':
    main()





if __name__ == '__main__':
    main()