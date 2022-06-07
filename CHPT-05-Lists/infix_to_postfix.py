"""
Exercise 131: Infix to Postfix

Mathematical expressions are often written in infix form, where operators appear
between the operands on which they act. While this is a common form, it is also
possible to express mathematical expressions in postfix form, where the operator
appears after all of its operands. For example, the infix expression 3 + 4 is written
as 3 4 + in postfix form. One can convert an infix expression to postfix form using
the following algorithm.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

# info: infix expression: 3 + 4 ; postfix expression: 3 4 +
# check conversions at https://www.mathblog.dk/tools/infix-postfix-converter/

from tokenizing_string import tokenList
from is_integer import isInteger
from operator_precedence import precedence

def infix_to_postfix(t):
    all_op = ['+', '-', '*', '/', '**', '^']
    operators = []
    postfix = []
    for token in t:
        if isInteger(token):
            postfix.append(token)
        if token in all_op:
            while operators != [] and operators[-1] != '(' and precedence(token) <= precedence(operators[-1]):
                postfix.append(operators.pop())
            operators.append(token)
        if token == '(':
            operators.append(token)
        if token == ')':
            while operators[-1] != '(':
                postfix.append(operators.pop())
            operators.remove('(')
    
    while len(operators) > 0:
        postfix.append(operators.pop())
    
    print(''.join(postfix))
    return postfix

def main():
    myexpression = input('Enter math expression: ')
    infix_to_postfix(tokenList(myexpression))

if __name__ == '__main__':
    main()
