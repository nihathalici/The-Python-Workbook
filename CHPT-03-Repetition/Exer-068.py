"""
Exercise 68: Compute a Grade Point Average

Exercise 52 includes a table that shows the conversion from letter grades to grade
points at a particular academic institution. In this exercise you will compute the
grade point average of an arbitrary number of letter grades entered by the user. The
user will enter a blank line to indicate that all of the grades have been provided. For
example, if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solution to Exercise 52 helpful when completing this exercise.
Your program does not need to do any error checking. It can assume that each value
entered by the user will always be a valid letter grade or a blank line.
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

grades = []

while True:
    grade = input("Enter an American grade: ")

    points = 0

    if grade == '':
        break
    if grade == 'A+':
        points = 4.0
    if grade == 'A':
        points = 4.0
    if grade == 'A-':
        points = 3.7
    if grade == 'B+':
        points = 3.3
    if grade == 'B':
        points = 3.0
    if grade == 'B-':
        points = 2.7
    if grade == 'C+':
        points = 2.3
    if grade == 'C':
        points = 2.0
    if grade == 'C-':
        points = 1.7
    if grade == 'D+':
        points = 1.3
    if grade == 'D':
        points = 1.0
    if grade == 'F':
        points = 0

    grades.append(points)

total = 0

num = 0

for grade in grades:
    total += grade
    num += 1

average = total / num

print("Your grade average is {}.".format(average))
