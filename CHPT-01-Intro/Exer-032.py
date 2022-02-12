
"""
Exercise 32: Sum of the Digits in an Integer

Develop a program that reads a four-digit integer from the user and displays the sum
of its digits. For example, if the user enters 3141 then your program should display
3 + 1 + 4 + 1 = 9.
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

number = input("Please enter a four digit integer: ")

sum = int(number[0])
sum += int(number[1])
sum += int(number[2])
sum += int(number[3])

print("The sum of the four digits in the number is {}.".format(sum))

"""

# Solution by Aldo Telese
# https://github.com/aldotele

value = int(input("Enter integer of four digits: "))

value_str = str(value)

sum_of_digits = int(value_str[0]) + int(value_str[1]) + int(value_str[2]) + int(value_str[3])

print(sum_of_digits)
"""



