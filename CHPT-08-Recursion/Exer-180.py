"""
Exercise 180: String Edit Distance

The edit distance between two strings is a measure of their similarity. The smaller the
edit distance, the more similar the strings are with regard to the minimum number of
insert, delete and substitute operations needed to transform one string into the other.
Consider the strings kitten and sitting. The first string can be transformed
into the second string with the following operations: Substitute the k with an s,
substitute the e with an i, and insert a g at the end of the string. This is the smallest
number of operations that can be performed to transform kitten into sitting.
As a result, the edit distance is 3.
Write a recursive function that computes the edit distance between two strings.
Use the following algorithm:

Use your recursive function to write a program that reads two strings from the
user and displays the edit distance between them.
"""

# Author's solution:
##
# Compute and display the edit distance between two strings.
#
## Compute the edit distance between two strings. The edit distance is the minimum number of
# insert, delete and substitute operations needed to transform one string into the other.
# @param s the first string
# @param t the second string
# @return the edit distance between the strings
def editDistance(s, t):
    # If one string is empty, then the edit distance is one insert operation for each letter in the
    # other string
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
        # If the last characters are not equal then set cost to 1
        if s[len(s) - 1] != t[len(t) - 1]:
            cost = 1

        # Compute three distances
        d1 = editDistance(s[0 : len(s) - 1], t) + 1
        d2 = editDistance(s, t[0 : len(t) - 1]) + 1
        d3 = editDistance(s[0 : len(s) - 1], t[0 : len(t) - 1]) + \
             cost

        # Return the minimum distance
        return min(d1, d2, d3)

# Compute the edit distance between two strings entered by the user
def main():
    # Read two strings from the user
    s1 = input("Enter a string: ")
    s2 = input("Enter another string: ")

    # Compute and display the edit distance
    print("The edit distance between %s and %s is %d." % \
          (s1, s2, editDistance(s1, s2)))

# Call the main function
main()
    
            
    
