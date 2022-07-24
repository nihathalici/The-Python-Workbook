"""
Exercise 183: Element Sequences

Some people like to play a game that constructs a sequence of chemical elements
where each element in the sequence begins with the last letter of its predecessor.
For example, if a sequence begins with Hydrogen, then the next element must be an
element that begins with N, such as Nickel. The element following Nickel must begin
with L, such as Lithium. The element sequence that is constructed cannot contain
any duplicates. When played alone the goal of the game is to constructed the longest
possible sequence of elements. When played with two players, the goal is to select
an element that leaves your opponent without an option to add to the sequence.

Write a program that reads the name of an element from the user and uses a
recursive function to find the longest sequence of elements that begins with that
value. Display the sequence once it has been computed. Ensure that your program
responds in a reasonable way if the user does not enter a valid element name.

HINT: It may take your program up to two minutes to find the longest sequence
for some elements. As a result, you might want to use elements like Molyb-
denum and Magnesium as your first test cases. Each has a longest sequence
that is only 8 elements long which your program should find in a fraction of a
second.
"""
# Author's solution:
##
# Identify the longest sequence of elements that can follow an element entered by the
# user where each element in the sequence begins with the same letter as the last letter
# of its predecessor.
#
ELEMENTS_FNAME = "elements.txt"

## Find the longest sequence of words, beginning with start, where each word begins with
# the last letter of its predecessor
# @param start the first word in the sequence
# @param words the list of words that can occur in the sequence
# @return the longest list of words beginning with start that meets the constraints
#    outlined previously
def longestSequence(start, words):
    # Base case: If start is empty then the list of words is empty
    if start == "":
        return []

    # Find the best (longest) list of words by checking each
    # possible word that could appear next in the sequence
    best = []
    last_letter = start[len(start) - 1].lower()
    for i in range(0, len(words)):
        first_letter = words[i][0].lower()

        # If the first letter of the next word matches
        # the last letter of the previous word
        if first_letter == last_letter:
            # Use recursion to find a candidate sequence of words
            candidate = longestSequence(words[i], \
                        words[0 : i] + words[i + 1 : len(words)])
            # Save the candidate if it is better than
            # the best sequence that we have seen previously
            if len(candidate) > len(best):
                best = candidate

    # Return the best candidate sequence, preceded by the starting word
    return [start] + best

## Load the names of all of the elements from the elements file
# @return a list of all the element names
def loadNames():
    names = []

    # Open the element data set
    inf = open(ELEMENTS_FNAME, "r")

    # Load each line, storing the element name in a list
    for line in inf:
        line = line.rstrip()
        parts = line.split(",")
        names.append(parts[2])

    # Close the file and return the list
    inf.close()
    return names

# Display a longest sequence of elements starting
# with an element entered by the user
def main():
    # Load all of the element names
    names = loadNames()

    # Read the starting element and capitalize it
    start = input("Enter the name of an element: ")
    start = start.capitalize()

    # Verify that the value entered by the user is an element
    if start in names:
        # Remove the starting element from the list of elements
        names.remove(start)

        # Find a longest sequence that begins with the starting element
        sequence = longestSequence(start, names)

        # Display the sequence of elements
        print("A longest sequence that starts with", start, "is:")
        for element in sequence:
            print(" ", element)
    else:
        print("Sorry, that wasn’t a valid element name.")

# Call the main function
main()
