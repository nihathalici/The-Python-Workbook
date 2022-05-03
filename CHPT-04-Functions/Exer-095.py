"""
Exercise 95: Capitalize It

Many people do not use capital letters correctly, especially when typing on small
devices like smart phones. To help address this situation, you will create a function
that takes a string as its only parameter and returns a new copy of the string that has
been correctly capitalized. In particular, your function must:

• Capitalize the first non-space character in the string,

• Capitalize the first non-space character after a period, exclamation mark or question
mark, and

• Capitalize a lowercase “i” if it is preceded by a space and followed by a space,
period, exclamation mark, question mark or apostrophe.

Implementing these transformations will correct most capitalization errors. For
example, if the function is provided with the string “what time do i have to be there?
what’s the address? this time i’ll try to be on time!” then it should return the string
“What time do I have to be there? What’s the address? This time I’ll try to be on
time!”. Include a main program that reads a string from the user, capitalizes it using
your function, and displays the result.
"""
# Author's solution:

##
# Improve the capitalization of a string.
#
## Capitalize the appropriate characters in a string
# @param s the string that needs capitalization
# @return a new string with the capitalization improved

def capitalize(s):
    # Create a new copy of the string to return as the function’s result
    result = s
    
    # Capitalize the first non-space character in the string
    pos = 0
    while pos < len(s) and result[pos] == ' ':
        pos = pos + 1

    if pos < len(s):
        # Replace the character with its uppercase version without changing any other characters
        result = result[0 : pos] + result[pos].upper() + \
                 result[pos + 1 : len(result)]

    # Capitalize the first letter that follows a ‘‘.’’, ‘‘!’’ or ‘‘?’’
    pos = 0
    while pos < len(s):
        if result[pos] == "." or result[pos] == "!" or \
           result[pos] == "?":
            # Move past the ‘‘.’’, ‘‘!’’ or ‘‘?’’
            pos = pos + 1

            # Move past any spaces
            while pos < len(s) and result[pos] == " ":
                pos = pos + 1

            # If we haven’t reached the end of the string then replace the current character
            # with its uppercase equivalent
            if pos < len(s):
                result = result[0 : pos] + \
                         result[pos].upper() + \
                         result[pos + 1 : len(result)]
        # Move to the next character
        pos = pos + 1

    # Capitalize i when it is preceded by a space and followed by a space, period, exclamation
    # mark, question mark or apostrophe
    pos = 1
    while pos < len(s) - 1:
        if result[pos - 1] == " " and result[pos] == "i" and \
           (result[pos + 1] == " " or result[pos + 1] == "." or \
            result[pos + 1] == "!" or result[pos + 1] == "?" or \
            result[pos + 1] == "’"):
            # Replace the i with an I without changing any other characters
            result  = result[0 : pos] + "I" + \
                      result[pos + 1 : len(result)]
        pos = pos + 1

    return result

# Demonstrate the capitalize function
def main():
    s = input("Enter some text: ")
    capitalized = capitalize(s)
    print("It is capitalized as:", capitalized)

main()
           
    
        
                
            
    
        
