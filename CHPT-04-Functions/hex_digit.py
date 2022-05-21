"""
Exercise 104: Hexadecimal and Decimal Digits

Write two functions, hex2int and int2hex, that convert between hexadecimal
digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) and decimal (base 10) integers.
The hex2int function is responsible for converting a string containing a single
hexadecimal digit to a base 10 integer, while the int2hex function is responsible
for converting an integer between 0 and 15 to a single hexadecimal digit. Each
function will take the value to convert as its only parameter and return the converted
value as its only result. Ensure that the hex2int function works correctly for both
uppercase and lowercase letters. Your functions should display a meaningful error
message and end the program if the parameter’s value is outside of the expected
range.
"""

def hex2int(hexa):

    if hexa.isdigit():  # checking if it is a number
        if 0 <= int(hexa) <= 9:
            integer = int(hexa)
            return integer

    hexa = hexa.upper()
    if hexa == 'A':
        integer = 10
    elif hexa == 'B':
        integer = 11
    elif hexa == 'C':
        integer = 12
    elif hexa == 'D':
        integer = 13
    elif hexa == 'E':
        integer = 14
    elif hexa == 'F':
        integer = 15
    else:
        return "That's not a hexadecimal."

    return integer


def int2hex(integer):
    if 0 <= integer <= 9:
        hexa = integer
        return hexa
    elif 10 <= integer <= 15:
        if integer == 10:
            hexa = 'A'
        elif integer == 11:
            hexa = 'B'
        elif integer == 12:
            hexa = 'C'
        elif integer == 13:
            hexa = 'D'
        elif integer == 14:
            hexa = 'E'
        else:
            hexa = 'F'
        return hexa
    else:
        return "No hexadecimal corresponding to that integer."


if __name__ == '__main__':
    h = input('Enter hexadecimal: ')
    print(hex2int(h))
    print()
    i = int(input('Enter integer: '))
    print(int2hex(i))
