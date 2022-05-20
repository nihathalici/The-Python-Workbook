"""
Exercise 117: Only the Words

In this exercise you will create a program that identifies all of the words in a
string entered by the user. Begin by writing a function that takes a string as
its only parameter. Your function should return a list of the words in the string
with the punctuation marks at the edges of the words removed. The punctuation marks
that you must consider include commas, periods, question marks,
hyphens, apostrophes, exclamation points, colons, and semicolons. Do not remove
punctuation marks that appear in the middle of a word, such as the apostrophes
used to form a contraction. For example, if your function is provided with the
string

"Contractions include: don’t, isn’t, and wouldn’t."

then your function should return the list
["Contractions", "include", "don’t", "isn’t", "and", "wouldn’t"].

Write a main program that demonstrates your function. It should read a string from
the user and then display all of the words in the string with the punctuation marks
removed. You will need to import your solution to this exercise when completing
Exercises 118 and 167. As a result, you should ensure that your main program only
runs when your file has not been imported into another program.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

def words_in_string(s):
    # splitting string based on spaces
    base_list = s.split()

    res_list = []

    # looping each element and removing, to the left and right, all specified characters
    for el in base_list:
        el = el.strip(",.?!-;:\"()")
        # adding that edited element to the results' list, only if it is not empty
        # note: a specific element might become empty if only made of the specified characters (e.g.  !!!)
        if el:
            # in the results' list there will only be words that start and end with a letter
            # words can have the specified characters in-between, but not to the sides
            res_list.append(el.lower())

    return res_list


def main():
    string = input('Enter a string: ')
    print(words_in_string(string))

if __name__ == '__main__':
    main()
