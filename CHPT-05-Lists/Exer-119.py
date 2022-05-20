"""
Exercise 119: Below and Above Average

Write a program that reads numbers from the user until a blank line is entered. Your
program should display the average of all of the values entered by the user. Then
the program should display all of the below average values, followed by all of the
average values (if any), followed by all of the above average values. An appropriate
label should be displayed before each list of values.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

numbers = []
n = input("Enter a number (blank to quit): ")
acc = 0

while n != '':
    n = int(n)
    acc += n 
    numbers.append(n)
    n = input("Enter a number (blank to quit): ")

avg = acc / len(numbers)

below_avg = []
above_avg = []
avg_values = []

for i in numbers:
    if i < avg:
        below_avg.append(i)
    elif i > avg:
        above_avg.append(i)
    else:
        avg_values.append(i)

print(numbers)
print('Average value: %.1f' % avg)
print('Below average values >>> {}'.format(below_avg))
if avg_values:
    print('Average values >>> {}'.format(avg_values))
print('Above average >>> {}'.format(above_avg))
