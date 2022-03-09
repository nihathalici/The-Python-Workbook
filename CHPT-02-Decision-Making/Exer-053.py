"""
Exercise 53: Grade Points to Letter Grade

In the previous exercise you created a program that converted a letter grade into the
equivalent number of grade points. In this exercise you will create a program that
reverses the process and converts from a grade point value entered by the user to a
letter grade. Ensure that your program handles grade point values that fall between
letter grades. These should be rounded to the closest letter grade. Your program
should report A+ if the value entered by the user is 4.0 or more.
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

points = float(input("Enter a number of grade points: "))

grade = ""


if points >= 0 and points < 0.5:
	grade = "F"
elif points >= 0.5 and points < 1.15:
	grade = "D"
elif points >= 1.5 and points < 1.5:
	grade = "D+"
elif points >= 1.5 and points < 1.85:
	grade = "C-"
elif points >= 1.85 and points < 2.15:
	grade = "C"
elif points >= 2.15 and points < 2.5:
	grade = "C+"
elif points >= 2.5 and points < 2.85:
	grade = "B-"
elif points >= 2.85 and points < 3.15:
	grade = "B"
elif points >= 3.15 and points < 3.5:
	grade = "B+"
elif points >= 3.5 and points < 3.85:
	grade = "A-"
elif points >= 3.85 and points < 4.0:
	grade = "A"
elif points >= 4.0:
	grade = "A+"
	
if grade != "":
	print("The closest grade is an {}.".format(grade))
else:
	print("Invalid number of grade points entered.")





