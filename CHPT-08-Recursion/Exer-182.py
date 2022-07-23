"""
Exercise 182: Spelling with Element Symbols

Each chemical element has a standard symbol that is one, two or three letters long.
One game that some people like to play is to determine whether or not a word can be
spelled using only element symbols. For example, silicon can be spelled using the
symbols Si, Li, C, O and N. However, hydrogen cannot be spelled with any combi-
nation of element symbols.

Write a recursive function that determines whether or not a word can be spelled
using only element symbols.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

from ntpath import altsep


symbols = []
elements = []
inf = open('elements.txt', 'r')
all_lines = inf.readlines()

for el in all_lines:
    # since the file includes the symbol between two commas, 
    # I separate the row in 3 elements dividid by a comma
    # I get the symbol by extracting the element in the middle
    # instead, extracting the last element I get the extended name of that element
    symbol = el.split(',')[1]
    element = el.split(',')[2].strip()
    # in this way I got the symbol and the element in each line, 
    # and I push them in their respective lists
    symbols.append(symbol)
    elements.append(element)

print(symbols)
print(elements)

res = ''

def symbolWord(string, symb_list):
    global res

    if string == '':
        return res
    
    else:
        if string[:3].capitalize() in symb_list:
            res += symb_list[symb_list.index(string[:3].capitalize())]
            string = string[3:]
            return symbolWord(string, symb_list)
        
        elif string[:2].capitalize() in symb_list:
            res += symb_list[symb_list.index(string[:2].capitalize())]
            string = string[2:]
            return symbolWord(string, symb_list)
        
        elif string[:1].capitalize() in symb_list:
            res += symb_list[symb_list.index(string[:1].capitalize())]
            string = string[1:]
            return symbolWord(string, symb_list)
        
        else:
            return False

if __name__ == '__main__':

    for element in elements:
        res = ''
        output = symbolWord(element, symbols)
        if output:
            print()
            print(element, 'can be spelled as:')
            print(output)

# print(symbolWord('Tin', symbols))

""" 
Aldo Tele's note:
TO FIX
for a word as "scatenare" it does not work properly because it takes first longer combinations, in this way:
sc is present
at is present
En is not present, thus it returns False
but if it did instead:
s is present
ca is present
te is present
na is present
re is present
then it would work
ALSO...
when printing all elements that can be formed by symbols, I have to reset res at each iteration
"""
