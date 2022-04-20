"""
Exercise 83: Maximum Integer

This exercise examines the process of identifying the maximum value in a collection
of integers. Each of the integers will be randomly selected from the numbers between
1 and 100. The collection of integers may contain duplicate values, and some of the
integers between 1 and 100 may not be present.
Take a moment and think about how you would solve this problem on paper. Many
people would check each integer in sequence and ask themself if the number that
they are currently considering is larger than the largest number that they have seen
previously. If it is, then they forget the previous maximum number and remember
the current number as the new maximum number. This is a reasonable approach,
and will result in the correct answer when the process is performed carefully. If you
were performing this task, how many times would you expect to need to update the
maximum value and remember a new number?
While we can answer the question posed at the end of the previous paragraph
using probability theory, we are going to explore it by simulating the situation. Cre-
ate a program that begins by selecting a random integer between 1 and 100. Save this
integer as the maximum number encountered so far. After the initial integer has been
selected, generate 99 additional random integers between 1 and 100. Check each
integer as it is generated to see if it is larger than the maximum number encountered
so far. If it is then your program should update the maximum number encountered
and count the fact that you performed an update. Display each integer after you gen-
erate it. Include a notation with those integers which represent a new maximum.
After you have displayed 100 integers your program should display the max-
imum value encountered, along with the number of times the maximum value
was updated during the process. Partial output for the program is shown below,
with... representing the remaining integers that your program will display. Run your
program several times. Is the number of updates performed on the maximum value
what you expected?

30
74 <== Update
58
17
40
37
13
34
46
52
80 <== Update
37
97 <== Update
45
55
73
...
The maximum value found was 100
The maximum value was updated 5 times
"""

# Author's solution:
##
# Find the maximum of 100 random integers and count the number of times the maximum value
# is updated during the process.
#
from random import randrange

NUM_ITEMS = 100

# Generate the first number and display it
mx_value = randrange(1, NUM_ITEMS + 1)
print(mx_value)

# Count the number of times the maximum value is updated
num_updates = 0

# For each of the remaining numbers
for i in range(1, NUM_ITEMS):
    # Generate a new random number
    current = randrange(1, NUM_ITEMS + 1)

    # If the generated number is the largest one we have seen so far
    if current > mx_value:
        # Update the maximum and count the update
        mx_value = current
        num_updates = num_updates + 1
        # Display the number, noting that an update occurred
        print(current, "<== Update")
    else:
        # Display the number
        print(current)

# Display the other results
print("The maximum value found was", mx_value)
print("The maximum value was updated", num_updates, "times")

        
    
