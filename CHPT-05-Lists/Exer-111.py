"""
Exercise 111: Reverse Order

Write a program that reads integers from the user and stores them in a list. Use 0 as
a sentinel value to mark the end of the input. Once all of the values have been read
your program should display them (except for the 0) in reverse order, with one value
appearing on each line.
"""
# Display a list of integers entered by the user in descending order.
#
# Start with an empty list
data = []

# Read values and add them to the list until the user enters 0
num = int(input("Enter an integer (0 to quit): "))

while num != 0:
    data.append(num)
    num = int(input("Enter an integer (0 to quit): "))

# Sort the values
data.sort(reverse=True)

# Display the values in descending order
print("The values, sorted into descending order, are:")
for num in data:
    print(num)
