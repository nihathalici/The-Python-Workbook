"""
Exercise 64: Discount Table

A particular retailer is having a 60 percent off sale on a variety of discontinued
products. The retailer would like to help its customers determine the reduced price
of the merchandise by having a printed discount table on the shelf that shows the
original prices and the prices after the discount has been applied. Write a program that
uses a loop to generate this table, showing the original price, the discount amount,
and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure
that the discount amounts and the new prices are rounded to 2 decimal places when
they are displayed.
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

for item in range(5):
    original = 5*item + 4.95
    discounted = original / 100 * 40

    print("Original: ${} | Discounted: ${} ".format(round(original, 2), round(discounted, 2)))
