"""
Exercise 110: Sorted Order

Write a program that reads integers from the user and stores them in a list. Your
program should continue reading values until the user enters 0. Then it should display
all of the values entered by the user (except for the 0) in ascending order, with one
value appearing on each line. Use either the sort method or the sorted function
to sort the list.
"""
# Author's solution:
##
# Display a list of integers entered by the user in ascending order.
#
# Start with an empty list
data = []

# Read values and add them to the list until the user enters 0
num = int(input("Enter an integer (0 to quit): "))

while num != 0:
    data.append(num)
    num = int(input("Enter an integer (0 to quit): "))

# Sort the values
data.sort()

# Display the values in ascending order
print("The values, sorted into ascending order, are:")
for num in data:
    print(num)

