"""
Exercise 133: Does a List Contain a Sublist?

A sublist is a list that is part of a larger list. A sublist may be a list containing a
single element, multiple elements, or even no elements at all. For example,
[1], [2], [3] and [4]
are all sublists of
[1, 2, 3, 4].
The list
[2, 3]
is also a sublist of
[1, 2, 3, 4],
but
[2, 4]
is not a sublist of
[1, 2, 3, 4]
because the elements 2 and 4 are not adjacent in the longer list. The empty list
is a sublist of any list. As a result,
[]
is a sublist of
[1, 2, 3, 4].
A list is a sublist of itself, meaning that
[1, 2, 3, 4]
is also a sublist of
[1, 2, 3, 4].
In this exercise you will create a function, isSublist, that determines whether
or not one list is a sublist of another. Your function should take two lists, larger
and smaller, as its only parameters. It should return True if and only if smaller
is a sublist of larger. Write a main program that demonstrates your function.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

def isSublist(larger, smaller):
    if smaller == [] or smaller == larger:
        return True
    """
    if smaller[0] in larger and len(smaller) == 1:
        return True
    """
    if smaller[0] not in larger or len(smaller) > len(larger):
        return False
    
    else:

        check = True
        # looping each element to find the elements that are equal 
        # to the first of smaller inside the larger list
        for i in range(len(larger)):
            if larger[i] == smaller[0]:
                sub_i = i + 1
                for j in range(1, len(smaller)):
                    if smaller[j] != larger[sub_i]:
                        check = False
                        break
                    else:
                        check = True
                    sub_i += 1
                # at the end of the loop I check if the value of check is still True
                if check:
                    return True
        return False

def main():
    print(isSublist([1, 2, 3, 4], []))
    print(isSublist([1, 2, 3, 4], [1]))
    print(isSublist([1, 2, 3, 4], [1, 2]))
    print(isSublist([1, 2, 3, 4], [2, 4]))
    print(isSublist([1, 2, 3, 4], [3, 4]))
    print(isSublist([10, 2, 35, 47, 10, 2, 36, 46, 10, 2, 35, 45, 46], [10, 2, 35, 46]))
    print(isSublist([10, 2, 35, 47, 10, 2, 36, 46, 10, 2, 35, 45, 46], [10, 2, 35, 45, 46]))
    print(isSublist([10, 2, 35, 47, 10, 2, 36, 46, 10, 2, 35, 45, 46], [10, 2, 35, 45, 45, 46]))

if __name__ == '__main__':
    main()


