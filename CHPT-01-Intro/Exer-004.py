"""
Exercise 4: Area of a Field

Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.

Hint: There are 43,560 square feet in an acre.
"""

wi = round(float(input("Enter the width in feet: ")))
le = round(float(input("Enter the length in feet: ")))
ar = wi * le / 43560 
print("The area is {} acres.".format(round(ar,2)))


"""
# Author's solution:
SQFT_PER_ACRE = 43560

length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))

acres = length * width / SQFT_PER_ACRE

print("The area of the field is", acres, "acres")
"""

