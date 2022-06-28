"""
Exercise 53: Grade Points to Letter Grade

In the previous exercise you created a program that converted a letter grade into the
equivalent number of grade points. In this exercise you will create a program that
reverses the process and converts from a grade point value entered by the user to a
letter grade. Ensure that your program handles grade point values that fall between
letter grades. These should be rounded to the closest letter grade. Your program
should report A+ if the value entered by the user is 4.0 or more.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

def point_to_lett(points):
    try:
        points = float(points)
    except:
        raise ValueError('Please enter a digit')

    if points >= 4:
        grade = "A+"
    elif points >= 3.86:
        grade = "A"
    elif points >= 3.5:
        grade = "A-"
    elif points >= 3.16:
        grade = "B+"
    elif points >= 2.86:
        grade = "B"
    elif points >= 2.5:
        grade = "B-"
    elif points >= 2.16:
        grade = "C+"
    elif points >= 1.86:
        grade = "C"
    elif points >= 1.5:
        grade = "C-"
    elif points >= 1.16:
        grade = "D+"
    elif points >= 0.86:
        grade = "D"
    elif 0 <= points < 0.86:
        grade = "F"
    else:
        raise ValueError('Negative digits are not allowed')

    return grade


def main():
    mygrade = input('Enter a point grade: ')
    print('{} corresponds to {}'.format(mygrade, point_to_lett(mygrade)))


if __name__ == '__main__':
    main()
