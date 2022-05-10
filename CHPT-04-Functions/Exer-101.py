"""
Exercise 101: Random License Plate

In a particular jurisdiction, older license plates consist of three letters followed by
three digits. When all of the license plates following that pattern had been used, the
format was changed to four digits followed by three letters.
Write a function that generates a random license plate. Your function should have
approximately equal odds of generating a sequence of characters for an old license
plate or a new license plate. Write a main program that calls your function and
displays the randomly generated license plate.

"""
from random import randint

A_ord = 65
Z_ord = 90
zero_ord = 48
nine_ord = 57

def random_license_plate():
    type_of_license = randint(1,2)
    license_plate = ''

    if type_of_license == 1:  # old license
        type_of_license = 'older'
        for i in range(3):
            random_letter = randint(A_ord, Z_ord)
            license_plate += chr(random_letter)
        for i in range(3):
            random_number = randint(zero_ord, nine_ord)
            license_plate += chr(random_number)
        return '%s (%s)' % (license_plate, type_of_license)

    if type_of_license == 2:  # new license
        type_of_license = 'newer'
        for i in range(4):
            random_number = randint(zero_ord, nine_ord)
            license_plate += chr(random_number)
        for i in range(3):
            random_letter = randint(A_ord, Z_ord)
            license_plate += chr(random_letter)
        return '%s (%s)' % (license_plate, type_of_license)


if __name__ == '__main__':
    print(random_license_plate())