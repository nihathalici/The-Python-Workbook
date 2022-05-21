"""
Exercise 100: Random Password

Write a function that generates a random password. The password should have a
random length of between 7 and 10 characters. Each character should be randomly
selected from positions 33 to 126 in the ASCII table. Your function will not take
any parameters. It will return the randomly generated password as its only result.
Display the randomly generated password in your file’s main program. Your main
program should only run when your solution has not been imported into another file.

Hint: You will probably find the chr function helpful when completing this
exercise. Detailed information about this function is available online.

"""

# Author's solution:
##
# Generate and display a random password containing between 7 and 10 characters.
#
from random import randint

SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126

## Generate a random password
# @return a string containing a random password
def randomPassword():
    # Select a random length for the password
    randomLength = randint(SHORTEST, LONGEST)

    # Generate an appropriate number of random characters,
    # adding each one to the end of result
    result = ""
    for i in range(randomLength):
        randomChar = chr(randint(MIN_ASCII, MAX_ASCII))
        result = result + randomChar

    # Return the random password
    return result

# Generate and display a random password
def main():
    print("Your random password is:", randomPassword())

# Call the main function only if the module is not imported
if __name__ == "__main__":
    main()
        
    

    
