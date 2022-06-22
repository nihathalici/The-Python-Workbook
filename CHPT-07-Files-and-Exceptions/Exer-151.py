"""
Exercise 151: Concatenate Multiple Files

Unix-based operating systems typically include a tool named cat, which is short for
concatenate. Its purpose is to display the concatenation of one or more files whose
names are provided as command line arguments. The files are displayed in the same
order that they appear on the command line.
"""
##
# Concatenate one or more files and display the result.
#
import sys

# Ensure that at least one command line argument (in addition to the .py file) has been provided
if len(sys.argv) == 1:
    print("You must provide at least one file name.")
    quit()

# Process all of the files provided on the command line
for i in range(1, len(sys.argv)):
    fname = sys.argv[i]
    try:
        # Open the current file for reading
        inf = open(fname, "r")

        # Display the file
        for line in inf:
            print(line,end="")

        # Close the file
        inf.close()
    except:

        # Display a message, but do not quit, so that the program will go on and process any
        # subsequent files
        print("Could't open/display", fname)
        
        
            
            
    
