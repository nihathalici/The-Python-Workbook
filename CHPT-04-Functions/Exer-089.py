"""
Exercise 89: Convert an Integer to Its Ordinal Number

Words like first, second and third are referred to as ordinal numbers. In this exercise,
you will write a function that takes an integer as its only parameter and returns a
string containing the appropriate English ordinal number as its only result. Your
function must handle the integers between 1 and 12 (inclusive). It should return an
empty string if the function is called with an argument outside of this range. Include
a main program that demonstrates your function by displaying each integer from 1
to 12 and its ordinal number. Your main program should only run when your file has
not been imported into another program.
"""

# Solution by Aldo Telese
# https://github.com/aldotele
# Modified by nihathalici


import random

def my_ordinal(n):
    if n < 1 or n > 12:
        return ''
    if n == 1:
        return 'first'
    elif n == 2:
        return 'second'
    elif n == 3:
        return 'third'
    elif n == 4:
        return 'fourth'
    elif n == 5:
        return 'fifth'
    elif n == 6:
        return 'sixth'
    elif n == 7:
        return 'seventh'
    elif n == 8:
        return 'eighth'
    elif n == 9:
        return 'ninth'
    elif n == 10:
        return 'tenth'
    elif n == 11:
        return 'eleventh'
    elif n == 12:
        return 'twelfth'
    

def main():
    print('Random ordinal between 1 and 12: ', end='')
    print(my_ordinal(random.randint(1, 12)))

    print()

    for i in range(1, 13):
        print("{}. {}".format(i, my_ordinal(i)))

if __name__ == '__main__':
    main()

