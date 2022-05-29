"""
Exercise 127: Is a List already in Sorted Order?

Write a function that determines whether or not a list of values is in sorted order
(either ascending or descending). The function should return True if the list is
already sorted. Otherwise it should return False. Write a main program that reads
a list of numbers from the user and then uses your function to report whether or not
the list is sorted.

Make sure you consider these questions when completing this exercise: Is a
list that is empty in sorted order? What about a list containing one element?
"""

# Solution by Aldo Telese
# https://github.com/aldotele

n = input('Enter a number: ')
t = []

while n != '':
    t.append(int(n))
    n = input('Enter a number (blank to quit): ')

def isSorted(li):
    return li == sorted(li)

print(isSorted(t))

