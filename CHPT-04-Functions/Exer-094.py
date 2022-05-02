"""
Exercise 94: Is It a Valid Triangle?

If you have 3 straws, possibly of differing lengths, it may or may not be possible
to lay them down so that they form a triangle when their ends are touching. For
example, if all of the straws have a length of 6 inches then one can easily construct
an equilateral triangle using them. However, if one straw is 6 inches long, while
the other two are each only 2 inches long, then a triangle cannot be formed. More
generally, if any one length is greater than or equal to the sum of the other two then
the lengths cannot be used to form a triangle. Otherwise they can form a triangle.

Write a function that determines whether or not three lengths can form a triangle.
The function will take 3 parameters and return a Boolean result. If any of the lengths
are less than or equal to 0 then your function should return False. Otherwise it
should determine whether or not the lengths can be used to form a triangle using
the method described in the previous paragraph, and return the appropriate result.
In addition, write a program that reads 3 lengths from the user and demonstrates the
behaviour of your function.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

def is_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True

def triangle_details(a, b, c):
    sum_bc = b + c
    sum_ac = a + c
    sum_ab = a + b

    if is_triangle(a, b, c):
        print("That's a triangle because:")
        print("a = %d < b + c = %d" % (a, sum_bc))
        print("b = %d < a + c = %d" % (b, sum_ac))
        print("c = %d < a + b = %d" % (c, sum_ab))
    else:
        print("That's not a triangle because:")
        if a >= sum_bc:
            print('a = %d >= b + c = %d' % (a, sum_bc))
        elif b >= sum_ac:
            print('b = %d >= a + c = %d' % (b, sum_bc))
        elif c >= sum_ab:
            print('c = %d >= a + b = %d' % (c, sum_ab))

def main():
    len1 = int(input("Enter length: "))
    len2 = int(input("Enter length: "))
    len3 = int(input("Enter length: "))
    triangle_details(len1, len2, len3)

if __name__ == '__main__':
    main()