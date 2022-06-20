"""
Exercise 149: Display the Head of a File

Unix-based operating systems usually include a tool named head. It displays the
first 10 lines of a file whose name is provided as a command line argument. Write
a Python program that provides the same behaviour. Display an appropriate error
message if the file requested by the user does not exist, or if the command line
argument is omitted.
"""
# Author's solution:
##
# Display the head (first 10 lines) of a file whose name is provided as a command line argument.
#
import sys

NUM_LINES = 10

# Verify that exactly one command line argument (in addition to the .py file) was supplied
if len(sys.argv) != 2:
    print("Provide the file name as a command line argument.")
    quit()

try:
    # Open the file for reading
    inf = open(sys.argv[1], "r")

    # Read the first line from the file
    line = inf.readline()

    # Keep looping until we have either read and displayed 10 lines or we have reached the end
    # of the file
    count = 0
    while count < NUM_LINES and line != "":
        # Remove the trailing newline character and count the line
        line = line.rstip()
        count = count + 1

        # Display the line
        print(line)

        # Read the next line from the file
        line = inf.readline()

    # Close the file
    inf.close()

except IOError:
    # Display a message if something goes wrong while accessing the file
    print("An error occurred while accessing the file.")
