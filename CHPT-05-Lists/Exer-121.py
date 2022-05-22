"""
Exercise 121: Random Lottery Numbers

In order to win the top prize in a particular lottery, one must match all 6 numbers
on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery
organizer. Write a program that generates a random selection of 6 numbers for a
lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates.
Display the numbers in ascending order.
"""

# Author's solution:
##
# Compute random but distinct numbers for a lottery ticket.
#
from random import randrange

MIN_NUM = 1
MAX_NUM = 49
NUM_NUMS = 6

# Use a list to store the numbers on the ticket
ticket_nums = []

# Generate NUM NUMS random but distinct numbers
for i in range(NUM_NUMS):
    # Generate a number that isn’t already on the ticket
    rand = randrange(MIN_NUM, MAX_NUM + 1)
    while rand in ticket_nums:
        rand = randrange(MIN_NUM, MAX_NUM + 1)

    # Add the number to the ticket
    ticket_nums.append(rand)
# Sort the numbers into ascending order and display them
ticket_nums.sort()
print("Your numbers are: ", end="")
for n in ticket_nums:
    print(n, end=" ")
print()
