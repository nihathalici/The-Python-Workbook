"""
Exercise 61: Is a License Plate Valid?

In a particular jurisdiction, older license plates consist of three uppercase letters
followed by three digits. When all of the license plates following that pattern had
been used, the format was changed to four digits followed by three uppercase letters.

Write a program that begins by reading a string of characters from the user. Then
your program should display a message indicating whether the characters are valid
for an older style license plate or a newer style license plate. Your program should
display an appropriate message if the string entered by the user is not valid for either
style of license plate.
"""

# Author's solution:

## Determine whether or not a license plate is valid. A valid license plate either consists of:
# 1) 3 letters followed by 3 numbers, or
# 2) 4 numbers followed by 3 numbers

# Read the plate from the user
plate = input("Enter the license plate: ")

# Check the status of the plate and display it. It is necessary to check each of the 6 characters
# for an older style plate, or each of the 7 characters for a newer style plate.
if len(plate) == 6 and \
   plate[0] >= "A" and plate[0] <= "Z" and \
   plate[1] >= "A" and plate[1] <= "Z" and \
   plate[2] >= "A" and plate[2] <= "Z" and \
   plate[3] >= "0" and plate[3] <= "9" and \
   plate[4] >= "0" and plate[4] <= "9" and \
   plate[5] >= "0" and plate[5] <= "9":
    print("The plate is a valid older style plate.")
elif len(plate) == 7 and \
   plate[0] >= "0" and plate[0] <= "9" and \
   plate[1] >= "0" and plate[1] <= "9" and \
   plate[2] >= "0" and plate[2] <= "9" and \
   plate[3] >= "0" and plate[3] <= "9" and \
   plate[4] >= "A" and plate[4] <= "Z" and \
   plate[5] >= "A" and plate[5] <= "Z" and \
   plate[6] >= "A" and plate[6] <= "Z":
    print("The plate is a valid newer style plate.")
else:
    print("The plate is not valid.")
