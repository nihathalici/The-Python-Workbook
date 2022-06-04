"""
Exercise 132: Evaluate Postfix

Evaluating a postfix expression is easier than evaluating an infix expression because
it does not contain any parentheses and there are no operator precedence rules to
consider. A postfix expression can be evaluated using the following algorithm:
"""

# Solution by Aldo Telese
# https://github.com/aldotele

from ast import Expression
from infix_to_postfix import infix_to_postfix
from tokenizing_string import tokenList
from is_integer import isInteger

def eval_postfix(postfixexp):
    values = []
    for token in postfixexp:
        if isInteger(token):
            token = int(token)
            values.append(token)
        else:
            right = values.pop()
            left = values.pop()
            # if it is an operator, I have to place it in-between two numbers extracted from values list
            # in order to compute the value of the created string, I use eval() which consider the string as python code
            # note: writing left and right as strings and I place the token string (an operator) in-between
            # eval() starts from my string of type "number operator number" and converts it in python code
            res = 'left' + token + 'right'
            values.append(eval(res))
    return values[0]

def main():
    expression = input('Enter a math expression: ')
    myinfix = tokenList(expression)
    mypostfix = infix_to_postfix(myinfix)
    print(mypostfix)
    print(eval_postfix(mypostfix))

if __name__ == '__main__':
    main()
