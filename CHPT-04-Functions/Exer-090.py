"""
Exercise 90: The Twelve Days of Christmas

The Twelve Days of Christmas is a repetitive song that describes an increasingly
long list of gifts sent to one’s true love on each of 12 days. A single gift is sent on
the first day. A new gift is added to the collection on each additional day, and then
the complete collection is sent. The first three verses of the song are shown below.
The complete lyrics are available on the Internet.

On the first day of Christmas
my true love sent to me:
A partridge in a pear tree.

On the second day of Christmas
my true love sent to me:
Two turtle doves,
And a partridge in a pear tree.

On the third day of Christmas
my true love sent to me:
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

Write a program that displays the complete lyrics for The Twelve Days of Christ-
mas. Your program should include a function that displays one verse of the song. It
will take the verse number as its only parameter. Then your program should call this
function 12 times with integers that increase from 1 to 12.

Each item that is sent to the recipient in the song should only appear in your
program once, with the possible exception of the partridge. It may appear twice if
that helps you handle the difference between “A partridge in a pear tree” in the first
verse and “And a partridge in a pear tree” in the subsequent verses. Import your
solution to Exercise 89 to help you complete this exercise.
"""

# Author's solution:

##
# Display the complete lyrics for the song The Twelve Days of Christmas.
#
from int_ordinal import intToOrdinal

## Display one verse of The Twelve Days of Christmas
# @param n the verse to display
# @return (None)

def displayVerse(n):
    print("On the", intToOrdinal(n), "day of Christmas")
    print("my true love sent to me:")

    if n >= 12:
        print("Twelve drummers drumming,")
    if n >= 11:
        print("Eleven pipers piping,")
    if n >= 10:
        print("Ten lords a-leaping,")
    if n >= 9:
        print("Nine ladies dancing,")
    if n >= 8:
        print("Eight maids a-milking,")
    if n >= 7:
        print("Seven swans a-swimming,")
    if n >= 6:
        print("Six geese a-laying,")
    if n >= 5:
        print("Five golden rings,")
    if n >= 4:
        print("Four calling birds,")
    if n >= 3:
        print("Three French hens,")
    if n >= 2:
        print("Two turtle doves",)
    if n == 1:
        print("A", end=" ")
    else:
        print("And a", end=" ")
    print("partridge in a pear tree.")
    print()

# Display all 12 verses of the song
def main():
    for verse in range(1, 13):
        displayVerse(verse)

main()
