"""
Exercise 185: Run-Length Decoding

Run-length encoding is a simple data compression technique that can be effec-
tive when repeated values occur at adjacent positions within a list. Compression
is achieved by replacing groups of repeated values with one copy of the value, fol-
lowed by the number of times that it should be repeated. For example, the list ["A",
"A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B",
"B", "B", "A", "A", "A", "A", "A", "A", "B"] would be compressed as
["A", 12, "B", 4, "A", 6, "B", 1]. Decompression is performed by repli-
cating each value in the list the number of times indicated.

Write a recursive function that decompresses a run-length encoded list. Your
recursive function will take a run-length compressed list as its only argument. It will
return the decompressed list as its only result. Create a main program that displays
a run-length encoded list and the result of decoding it.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

def decode(data):
    # BASE CASE
    if len(data) == 0:
        return []
    # RECURSIVE CASE
    else:
        current = list(data[0] * data[1])
        return current + decode(data[2:])

    # the output list will be a list where each letter appears as many times as the number just after it
    # the 'current' output list is made by multiplying the first element of the sublist by the second one
    # the current lists obtained through sub-lists will be added in order to return a single list
    # the recursion stops when the next sublist will be empty

def main():
    # specifying the compressed list I will use as a parameter
    # It can be changed to test the function for different parameters
    mylist = ['A', 3, 'B', 2, 'C', 6, 'D', 1, 'E', 5]
    print(decode(mylist))
    
if __name__ == '__main__':
    main()
