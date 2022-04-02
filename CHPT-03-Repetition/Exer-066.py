"""
Exercise 66: No More Pennies

February 4, 2013 was the last day that pennies were distributed by the Royal Canadian
Mint. Now that pennies have been phased out retailers must adjust totals so that they
are multiples of 5 cents when they are paid for with cash (credit card and debit card
transactions continue to be charged to the penny). While retailers have some freedom
in how they do this, most choose to round to the closest nickel.
Write a program that reads prices from the user until a blank line is entered.
Display the total cost of all the entered items on one line, followed by the amount
due if the customer pays with cash on a second line. The amount due for a cash
payment should be rounded to the nearest nickel. One way to compute the cash
payment amount is to begin by determining how many pennies would be needed to
pay the total. Then compute the remainder when this number of pennies is divided
by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust
the total up.
"""

# Author's solution
# Compute the total due when several items are purchased. The amount payable for cash
# transactions is rounded to the closest nickel because pennies have been phased out in Canada.

PENNIES_PER_NICKEL = 5
NICKEL = 0.05

# Track the total cost for all of the items
total = 0.00

# Read the price of the first item as a string
line = input("Enter the price of the item (blank to quit): ")

# Continue reading items until a blank line is entered
while line != "":
    # Add the cost of the item to the total (after converting it to a floating-point number)
    total = total + float(line)

    # Read the cost of the next item
    line = input("Enter the price of the item (blank to quit): ")

# Display the exact total payable
print("The exact amount payable is %.02f" % total)

# Compute the number of pennies that would be left if the total was paid using nickels
rounding_indicator  = total * 100 % PENNIES_PER_NICKEL

if rounding_indicator < PENNIES_PER_NICKEL / 2:
    # If the number of pennies left is less than 2.5 then we round down by subtracting that
    # number of pennies from the total
    cash_total = total - rounding_indicator / 100
else:
    # Otherwise we add a nickel and then subtract that number of pennies
    cash_total = total + NICKEL - rounding_indicator / 100

# Display amount due when paying with cash
print("The cash amount payable is %.02f" % cash_total)
