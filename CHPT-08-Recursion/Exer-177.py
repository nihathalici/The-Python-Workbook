"""
Exercise 177: Roman Numerals

As the name implies, Roman numerals were developed in ancient Rome. Even after
the Roman empire fell, its numerals continued to be widely used in Europe until the
late middle ages, and its numerals are still used in limited circumstances today.

Roman numerals are constructed from the letters M, D, C, L, X, V and I which
represent 1000, 500, 100, 50, 10, 5 and 1 respectively. The numerals are generally
written from largest value to smallest value. When this occurs the value of the number
is the sum of the values of all of its numerals. If a smaller value precedes a larger
value then the smaller value is subtracted from the larger value that it immediately
precedes, and that difference is added to the value of the number. 

Create a recursive function that converts a Roman numeral to an integer. Your
function should process one or two characters at the beginning of the string, and
then call itself recursively on all of the unprocessed characters. Use an empty string,
which has the value 0, for the base case. In addition, write a main program that reads
a Roman numeral from the user and displays its value. You can assume that the value
entered by the user is valid. Your program does not need to do any error checking.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

"""
M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1
when all numerals are in descendent order:
XVII = 10+5+2 = 17
when not all numerals are in descendent order:
XIV = 10+(5-1) = 14
"""

def roman_value(s):
    if s == 'M':
        return 1000
    elif s == 'D':
        return 500
    elif s == 'C':
        return 100
    elif s == 'L':
        return 50
    elif s == 'X':
        return 10
    elif s == 'V':
        return 5
    elif s == 'I':
        return 1
    else:
        raise ValueError('Not a valid roman numeral')

def roman_to_integer(roman):
    # BASE CASE
    # if there are no numeral left, 
    # I add zero to the sum and recursion ends
    if roman == '':
        return 0
    
    # if there is one numeral left, 
    # I add its value to the sum
    if len(roman) == 1:
        return roman_value(roman)
    
    # if there are still two numerals, I convert 
    # them in integer in order to compare them
    preceding = roman_value(roman[0])
    following = roman_value(roman[1])

    # if the preceding is a higher value, I add it to 
    # the sum and call the function again from the following
    if preceding >= following:
        return preceding + roman_to_integer(roman[1:])
    
    # if the preceding is lower, I subtract it from the 
    # following and add the subtraction to the sum
    # then I call the function again but from the 
    # numeral which comes next to the following
    elif preceding < following:
        return (following - preceding) + roman_to_integer(roman[2:])

if __name__ == '__main__':
    roman_number = input('Enter a roman number: ')
    print(roman_to_integer(roman_number))