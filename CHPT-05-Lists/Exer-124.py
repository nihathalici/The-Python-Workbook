"""
Exercise 124: Line of Best Fit

A line of best fit is a straight line that best approximates a collection of n data points.
In this exercise, we will assume that each point in the collection has an x coordinate
and a y coordinate. The symbols x̄ and ȳ are used to represent the average x value in
the collection and the average y value in the collection respectively. The line of best
fit is represented by the equation y = mx + b where m and b are calculated using
the following formulas:

Write a program that reads a collection of points from the user. The user will enter
the first x coordinate on its own line, followed by the first y coordinate on its own
line. Allow the user to continue entering coordinates, with the x and y values each
entered on their own line, until your program reads a blank line for the x coordinate.
Display the formula for the line of best fit in the form y = mx + b by replacing m
and b with the values calculated by the preceding formulas. For example, if the user
inputs the coordinates (1, 1), (2, 2.1) and (3, 2.9) then your program should display
y = 0.95x + 0.1.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

all_x = []
all_y = []
all_xy = []
all_xsquare = []

x = input("Enter x: ")
y = input("Enter y: ")
n = 0

while True:
    n += 1
    x = float(x)
    y = float(y)
    all_x.append(x)
    all_y.append(y)
    xy = x * y
    xsquare = x ** 2
    all_xy.append(xy)
    all_xsquare.append(xsquare)
    x = input("Enter x (blank to quit): ")
    if x == '':
        break
    y = input("Enter y: ")

sum_x = sum(all_x)
sum_y = sum(all_y)
sum_xy = sum(all_xy)
sum_xsquare = sum(all_xsquare)
avg_x = sum_x /n
avg_y = sum_y/ n

m_numerator = sum_xy - (sum_x * sum_y) / n
m_denominator =sum_xsquare - (sum_x ** 2) / n
m = m_numerator / m_denominator
b = avg_y - m * avg_x

print('y = %.2fx + %.2f' % (m, b))


print('sum of x is %d'%sum_x)
print('sum of y is %d'%sum_y)
print('sum of xy is %d'%sum_xy)
print('avg x is %.1f'%avg_x)
print('avg y is %.1f'%avg_y)


    
