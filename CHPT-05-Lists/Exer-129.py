"""
Exercise 129: Tokenizing a String

Tokenizing is the process of converting a string into a list of substrings, known as
tokens. In many circumstances, a list of tokens is far easier to work with than the
original string because the original string may have irregular spacing. In some cases
substantial work is also required to determine where one token ends and the next one
begins.
In a mathematical expression, tokens are items such as operators, numbers and
parentheses. The operator symbols that we will consider in this (and subsequent)
problems are *, /, ˆ, - and +. Operators and parentheses are easy to identify because
the token is always a single character, and the character is never part of another token.
Numbers are slightly more challenging to identify because the token may consist of
multiple characters. Any sequence of consecutive digits should be treated as one
number token.
Write a function that takes a string containing a mathematical expression as its
only parameter and breaks it into a list of tokens. Each token should be a parenthesis,
an operator, or a number. (For simplicity we will only work with integers in this
problem). Return the list of tokens as the function’s only result.
You may assume that the string passed to your function always contains a valid
mathematical expression consisting of parentheses, operators and integers. However,
your function must handle variable amounts of whitespace (including no whitespace)
between these elements. Include a main program that demonstrates your tokenizing
function by reading an expression from the user and printing the list of tokens. Ensure
that the main program will not run when the file containing your solution is imported
into another program.
"""
# Author's solution:
##
# Tokenize a string containing a mathematical expression.
#
## Convert a mathematical expression into a list of tokens
# @param s the string to tokenize
# @return a list of the tokens in s, or an empty list if an error occurs
def tokenList(s):
    # Remove all of the spaces from s
    s = s.replace(" ", "")
    # Loop through all of the characters in the string,
    # identifying the tokens and adding them to the list
    tokens = []
    i = 0
    while i < len(s):
        # Handle the tokens that are always a single character: *, /, ˆ, ( and )
        if s[i] == "*" or s[i] == "/" or s[i] == "^" or \
           s[i] == "(" or s[i] == ")" or s[i] == "+" or s[i] == "-":
            tokens.append(s[i])
            i = i + 1
        # Handle a number without a leading + or -
        elif s[i] >= "0" and s[i] <= "9":
            num = ""
            # Keep on adding characters to the token as long as they are digits
            while i < len(s) and s[i] >= "0" and s[i] <= "9":
                num = num + s[i]
                i = i + 1
            tokens.append(num)
        else:
            return []

    return tokens

def main():
    exp = input("Enter a mathematical expression: ")
    tokens = tokenList(exp)
    print("The tokens are:", tokens)

if __name__ == "__main__":
    main()
