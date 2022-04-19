"""
Exercise 81: Binary to Decimal

Write a program that converts a binary (base 2) number to decimal (base 10). Your
program should begin by reading the binary number from the user as a string. Then
it should compute the equivalent decimal number by processing each digit in the
binary number. Finally, your program should display the equivalent decimal number
with an appropriate message.
"""

# Solution by Aldo Telese
# https://github.com/aldotele
# Corrected by nihathalici

"""
conversion logic:
1010 is 10 namely 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 = 2^3 + 2 = 10
10010 is 18 namely 2^4 + 2
11011 is 27 ---> note that if the first value to the right is 1 it will be 1*2^0 = 1
"""

binary = input('Enter binary number: ')
decimal = 0

# Since I start reading from left in the string, I start raising to the highest power
power = len(binary) - 1

# Using the index to loop on each binary number
i= 0

# Loop continues until getting to power zero namely the last number to the right
while power >= 0:
    # Using the conversion rule at each iteration
    decimal += int(binary[i]) * 2 ** power
    # Reducing power when moving to the right
    power -= 1
    # Increasing index to iterate towards right
    i += 1

print('The decimal of %s is %d' % (binary, decimal))

