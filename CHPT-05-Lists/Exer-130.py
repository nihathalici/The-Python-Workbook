"""
Exercise 130: Unary and Binary Operators

Some mathematical operators are unary while others are binary. Unary operators act
on one value while binary operators act on two. For example, in the expression 2 *
-3 the * is a binary operator because it acts on both the 2 and the −3 while the - is
a unary operator because it only acts on the 3.

An operator’s symbol is not always sufficient to determine whether it is unary or
binary. For example, while the - operator was unary in the previous expression, the
same character is used to represent the binary - operator in an expression such as
2 - 3. This ambiguity, which is also present for the + operator, must be removed
before other interesting operations can be performed on a list of tokens representing
a mathematical expression.

Create a function that identifies unary + and - operators in a list of tokens and
replaces them with u+ and u- respectively. Your function will take a list of tokens
for a mathematical expression as its only parameter and return a new list of tokens
where the unary + and - operators have been substituted as its only result. A +
or - operator is unary if it is the first token in the list, or if the token that imme-
diately precedes it is an operator or open parenthesis. Otherwise the operator is
binary.

Write a main program that demonstrates that your function works correctly by
reading, tokenizing, and marking the unary operators in an expression entered by
the user. Your main program should not execute when your function is imported into
another program.
"""
# Author's solution:
##
# Differentiate between unary and binary + and - operators.
#
from token_list import tokenList

## Identify occurrences of unary + and - operators within a list of tokens and replace them
# with u+ and u- respectively
# @param tokens a list of tokens that may include unary + and - operators
# @return a list of tokens where unary + and - operators have been replaced with u+ and u-
def identifyUnary(tokens):
    retval = []

    # Process each token in the list
    for i in range(len(tokens)):
        # If the first token in the list is + or - then it is a unary operator
        if i == 0 and (tokens[i] == "+" or tokens[i] == "-"):
            retval.append("u" + tokens[i])
        # If the token is a + or - and the previous token is an operator or an open parenthesis
        # then it is a unary operator
        elif i > 0 and (tokens[i] == "+" or tokens[i] == "-") and \
             (tokens[i-1] == "+" or tokens[i-1] == "-" or
              tokens[i-1] == "*" or tokens[i-1] == "/" or
              tokens[i-1] == "("):
            retval.append(tokens[i])
    return retval

# Demonstrate that unary operators are marked correctly
def main():
    # Read an expression from the user, tokenize it, and display the result
    exp = input("Enter a mathematical expression: ")
    tokens = tokenList(exp)
    print("The tokens are:", tokens)

    # Identify the unary operators in the list of tokens
    marked = identifyUnary(tokens)
    print("With unary operators marked: ", marked)

# Call the main function only if this file has not been imported into another program
if __name__ == "__main__":
    main()
    
    
            
        

    



