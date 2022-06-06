"""
Exercise 134: Generate All Sublists of a List

Using the definition of a sublist from Exercise 133, write a function that returns a
list containing every possible sublist of a list. For example, the sublists of
[1, 2, 3]
are
[], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3].
Note that your function will always return a list containing at least the empty list
because the empty list is a sublist of every list. Include a main program that
demonstrate your function by displaying all of the sublists of several different lists.
"""
# Author's solution:
##
# Compute all of the sublists of a list.
#
## Generate a list of of all of the sublists of a list
# @param data the list for which the sublists are generated
# @return a list containing all of the sublists of data
def allSublists(data):
    # Start out with the empty list as the only sublist of data
    sublists = [[]]

    # Generate all of the sublists of data from length 1 to len(data)
    for length in range(1, len(data) + 1):
        # Generate the sublists starting at each index
        for i in range(0, len(data) - length + 1):
            # Add the current sublist to the list of sublists
            sublists.append(data[i : i + length])

    # Return the result
    return sublists

# Demonstrate the allSublists function
def main():
    print("The sublists of [] are: ")
    print(allSublists([]))

    print("The sublists of [1] are: ")
    print(allSublists([1]))

    print("The sublists of [1, 2] are: ")
    print(allSublists([1, 2]))

    print("The sublists of [1, 2, 3] are: ")
    print(allSublists([1, 2, 3]))

    print("The sublists of [1, 2, 3, 4] are: ")
    print(allSublists([1, 2, 3, 4]))

main()
