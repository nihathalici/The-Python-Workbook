"""
Exercise 174: Greatest Common Divisor

Euclid was a Greek mathematician who lived approximately 2,300 years ago. His
algorithm for computing the greatest common divisor of two positive integers, a and
b, is both efficient and recursive. It is outlined below:

  If b is 0 then
    Return a
  Else
    Set c equal to the remainder when a is divided by b
  Return the greatest common divisor of b and c

Write a program that implements Euclid’s algorithm and uses it to determine the
greatest common divisor of two integers entered by the user. Test your program with
some very large integers. The result will be computed quickly, even for huge numbers
consisting of hundreds of digits, because Euclid’s algorithm is extremely efficient.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

def find_gcd(a, b):
    # BASE CASE
    if b == 0:
        return a
    # RECURSIVE CASE
    else:
        c = a % b
        return find_gcd(b, c)

if __name__ == '__main__':
    print(find_gcd(0, 10))
