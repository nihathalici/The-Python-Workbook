"""
Exercise 102: Check a Password

In this exercise you will write a function that determines whether or not a password
is good. We will define a good password to be a one that is at least 8 characters long
and contains at least one uppercase letter, at least one lowercase letter, and at least
one number. Your function should return True if the password passed to it as its
only parameter is good. Otherwise it should return False. Include a main program
that reads a password from the user and reports whether or not it is good. Ensure
that your main program only runs when your solution has not been imported into
another file.
"""

# Author's solution:
##
# Check whether or not a password is good.
#
## Check whether or not a password is good. A good password is at least 8 characters and
# contains an uppercase letter, a lowercase letter and a number.
# @param password the password to check
# @return True if the password is good, False otherwise

def checkPassword(password):
    has_upper = False
    has_lower = False
    has_num = False

    # Check each character in the password and see which requirement it meets
    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_num = True

    # If the password has all 4 properties
    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    return False

def main():
    p = input("Enter a password: ")
    if checkPassword(p):
        print("That's a good password.")
    else:
        print("That isn't a good password.")

# Call the main function only if the file has not been imported into another program
if __name__ == "__main__":
    main()
        

        

    
