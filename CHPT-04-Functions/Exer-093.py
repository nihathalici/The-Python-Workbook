"""
Exercise 93: Center a String in the Terminal Window

Write a function that takes a string, s, as its first parameter, and the width of the
window in characters, w, as its second parameter. Your function will return a new
string that includes whatever leading spaces are needed so that s will be centered in
the window when the new string is printed. The new string should be constructed in
the following manner:

* If the length of s is greater than or equal to the width of the window then s should
be returned.

* If the length of s is less than the width of the window then a string containing
(len(s) - w) // 2 spaces followed by s should be returned.

Write a main program that demonstrates your function by displaying multiple
strings centered in the window.
"""

# Author's solution:
##
# Center a string of characters within a certain width.
#
from unittest import result


WIDTH = 80

## Create a new string that will be centered within a given width when it is printed.
# @param s the string that will be centered
# @param width the width in which the string will be centered
# @return a new copy of s that contains the leading spaces needed to center s
def center(s, width):
    # If the string is too long to center, then the original string is returned
    if width < len(s):
        return s
    
    # Compute the number of spaces needed and generate the result
    spaces = (width - len(s)) // 2
    result = " " * spaces + s

    return result

# Demonstrate the center function
def main():
    print(center("A Famous Story", WIDTH))
    print(center("by:", WIDTH))
    print(center("Someone Famous", WIDTH))
    print()
    print("Once upon a time...")

main()




