"""
Exercise 52: Letter Grade to Grade Points

At a particular university, letter grades are mapped to grade points in the following
manner:

---------------------
Letter  Grade Points
---------------------

A+      4.0         
A       4.0
A-      3.7
B+      3.3
B       3.0
B-      2.7
C+      2.3
C       2.0
C-      1.7
D+      1.3
D       1.0
F       0
---------------------

Write a program that begins by reading a letter grade from the user. Then your
program should compute and display the equivalent number of grade points. Ensure
that your program generates an appropriate error message if the user enters an invalid
letter grade.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

def lett_to_point(grade):
    try:
        grade = grade.upper()
    except:
        raise ValueError('Please enter a letter grade')

    if grade == "F":
        points = 0
    elif grade == "D":
        points = 1
    elif grade == "D+":
        points = 1.3
    elif grade == "C-":
        points = 1.7
    elif grade == "C":
        points = 2
    elif grade == "C+":
        points = 2.3
    elif grade == "B-":
        points = 2.7
    elif grade == "B":
        points = 3
    elif grade == "B+":
        points = 3.3
    elif grade == "A-":
        points = 3.7
    elif grade == "A" or grade == "A+":
        points = 4
    else:
        raise ValueError('Please enter a letter grade between A and F (+ or - can be included)')

    return points


def main():
    mygrade = input('Enter a letter grade: ')
    print('{} corresponds to {} points'.format(mygrade.upper(), lett_to_point(mygrade)))


if __name__ == '__main__':
    main()
