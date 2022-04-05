"""
Exercise 69: Admission Price

A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge. Children between 3 and
12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
for all other guests is $23.00.

Create a program that begins by reading the ages of all of the guests in a group
from the user, with one age entered on each line. The user will enter a blank line to
indicate that there are no more guests in the group. Then your program should display
the admission cost for the group with an appropriate message. The cost should be
displayed using two decimal places.
"""

# Author's solution:

##
# Compute the admission price for a group visiting the zoo.
#
# Store the admission prices as constants
BABY_PRICE = 0.00
CHILD_PRICE = 14.00
ADULT_PRICE = 23.00
SENIOR_PRICE = 18.00
# Store the age limits as constants
BABY_LIMIT = 2
CHILD_LIMIT = 12
ADULT_LIMIT = 64
# Create a variable to hold the total admission cost for all guests
total = 0

# Keep on reading ages until the user enters a blank line
line = input("Enter the age of the guest (blank to finish): ")
while line != "":
    age = int(line)

    # Add the correct amount to the total
    if age <= BABY_LIMIT:
        total = total + BABY_PRICE
    elif age <= CHILD_LIMIT:
        total = total + CHILD_PRICE
    elif age <= ADULT_LIMIT:
        total = total + ADULT_PRICE
    else:
        total = total + SENIOR_PRICE

    # Read the next age from the user
    line = input("Enter the age of the guest (blank to finish): ")

print("The total for that group is $%.2f" % total)
