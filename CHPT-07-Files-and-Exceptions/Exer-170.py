"""
Exercise 170: Missing Comments
(Solved, 48 Lines)
When one writes a function, it is generally a good idea to include a comment that
outlines the function’s purpose, its parameters and its return value. However, some-
times comments are forgotten, or left out by well-intentioned programmers that plan
to write them later but then never get around to it.
Create a Python program that reads one or more Python source files and identifies
functions that are not immediately preceded by a comment.
"""
# Author's solution:
##
# Find and display the names of Python functions that are not immediately preceded by a
# comment.
#
from sys import argv

# Verify that at least one file name has been provided as a command line argument
if len(argv) == 1:
    print("At least one filename must be provided as a", \
          "command line argument.")
    print("Quitting...")
    quit()

# Process each file provided as a command line argument
for fname in argv[1 : len(argv)]:
    # Attempt to process the file
    try:
        inf = open(fname, "r")

        # As we move through the file we need to keep a copy of the previous line so that we
        # can check to see if it starts with a comment character. We also need to keep track
        # of the line number within the file.
        prev = " "
        lnum = 1


        # Check each line in the current file
        for line in inf:
            # If the line is a function definition and the previous line is not a comment
            if line.startswith("def ") and prev[0] != "#":
                # Find the first ( on the line so that we know where the function name ends
                bracket_pos = line.index("(")
                name = line[4 : bracket_pos]

                # Display information about the function that is missing its comment
                print("%s line %d; %s" % (fname, lnum, name))

            # Save the current line and update the line counter
            prev = line
            lnum = lnum + 1

        # Close the current file
        inf.close()

    except:
        print("A problem was encountered with file '%s'." % fname)
        print("Moving on to the next file...")
                
            
    
