"""
Exercise 136: Reverse Lookup

Write a function named reverseLookup that finds all of the keys in a dictionary
that map to a specific value. The function will take the dictionary and the value to
search for as its only parameters. It will return a (possibly empty) list of keys from
the dictionary that map to the provided value.

Include a main program that demonstrates the reverseLookup function as part
of your solution to this exercise. Your program should create a dictionary and then
show that the reverseLookup function works correctly when it returns multiple
keys, a single key, and no keys. Ensure that your main program only runs when
the file containing your solution to this exercise has not been imported into another
program.

"""

# Author's solution:
##
# Conduct a reverse lookup on a dictionary, finding all of the keys that map to the provided
# value.
#
## Conduct a reverse lookup on a dictionary
# @param data the dictionary on which the reverse lookup is performed
# @param value the value to search for in the dictionary
# @return a list (possibly empty) of keys from data that map to value

def reverseLookup(data, value):
    # Construct a list of the keys that map to value
    keys = []

    # Check each key and add it to keys if the values match
    for key in data:
        if data[key] == value:
            keys.append(key)

    # Return the list of keys
    return keys

# Demonstrate the reverseLookup function
def main():
    # A dictionary mapping 4 French words to their English equivalents
    frEn = {"le" : "the", "la" : "the", "livre" : "book", \
            "pomme" : "apple"}

    # Demonstrate the reverseLookup function with 3 cases: One that returns multiple keys,
    # one that returns one key, and one that returns no keys
    print("The french words for 'the' are: ", \
          reverseLookup(frEn, "the"))
    print("Expected: ['le', 'la']")
    print()
    print("The french word for ’apple’ is: ", \
          reverseLookup(frEn, "apple"))
    print("Expected: ['pomme']")
    print()
    print("The french word for ’asdf’ is: ", \
          reverseLookup(frEn, "asdf"))
    print("Expected: []")

# Call the main function only if this file has not been imported into another program
if __name__ == "__main__":
    main()
