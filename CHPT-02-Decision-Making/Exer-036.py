"""
Exercise 36: Dog Years

It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.
Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

human_age = int(input("Enter a human age: "))

if human_age == 1:
    dog_age = 10.5
if human_age == 2:
    dog_age = 21
# from third human year, each year corresponds to four dog years
if human_age >= 3:
    dog_age = 21 + (human_age - 2) * 4
else:
    print("Please enter a valid age")
    exit()

print("A human age of {} equals a dog age of {}".format(human_age, dog_age))


"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

humanYearsOld = int(input("Please enter the age of a dog in human years: "))
	
if humanYearsOld <= 2:
	dogYears = humanYearsOld * 10.5
elif humanYearsOld > 2:
	dogYears = 2 * 10.5
	dogYears += (humanYearsOld-2) * 4

if humanYearsOld == 0:
	print("Please enter a positive integer.")
else:
	print("The dog is {} years old in dog years.".format(dogYears))

"""

