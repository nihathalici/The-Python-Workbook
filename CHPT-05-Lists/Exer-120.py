"""
Exercise 120: Formatting a List

When writing out a list of items in English, one normally separates the items with
commas. In addition, the word “and” is normally included before the last item, unless
the list only contains one item. Consider the following four lists:

apples
apples and oranges
apples, oranges and bananas
apples, oranges, bananas and lemons

Write a function that takes a list of strings as its only parameter. Your function
should return a string that contains all of the items in the list, formatted in the manner
described previously, as its only result. While the examples shown previously only
include lists containing four elements or less, your function should behave correctly
for lists of any length. Include a main program that reads several items from the user,
formats them by calling your function, and then displays the result returned by the
function.
"""
# Author's solution:
#
##
# Display a list of items so that they are separated by commas and the word ‘‘and’’ appears
# between the final two items.
#
## Format a list of items so that they are separated by commas and ‘‘and’’
# @param items the list of items to format
# @return a string containing the items with the desired formatting
def formatList(items):
    # Handle lists of 0 and 1 items as special cases
    if len(items) == 0:
        return "<empty>"
    if len(items) == 1:
        return str(items[0])

    # Loop over all of the items in the list except the last two
    result = ""
    for i in range(0, len(items) - 2):
        result = result + str(items[i]) + ", "

    # Add the second last and last items to the result, separated by ‘‘and’’
    result = result + str(items[len(items) - 2]) + " and "
    result = result + str(items[len(items) - 1])

    # Return the result
    return result

# Read several items entered by the user and display them with nice formatting
def main():
    # Read items from the user until a blank line is entered
    items = []
    line = input("Enter an item (blank to quit): ")
    while line != "":
        items.append(line)
        line = input("Enter an item (blank to quit): ")
    # Format and display the items:
    print("The items are %s." % formatList(items))

# Call the main function
main()
        
