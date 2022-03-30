"""
Exercise 65: Temperature Conversion Table

Write a program that displays a temperature conversion table for degrees Celsius and
degrees Fahrenheit. The table should include rows for all temperatures between 0
and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
headings on your columns. The formula for converting between degrees Celsius and
degrees Fahrenheit can be found on the Internet.
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

print("Celsius\t | Fahrenheit")

for celsiusTemp in range(0, 101, 10):
    fahrenheitTemp = (celsiusTemp * 9/5) + 32
    print("{}\t | {}".format(celsiusTemp, fahrenheitTemp))
