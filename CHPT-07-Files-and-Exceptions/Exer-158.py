    """
Exercise 158: Remove Comments

Python uses the # character to mark the beginning of a comment. The comment
continues from the # character to the end of the line containing it. Python does not
provide any mechanism for ending a comment before the end of a line.
In this exercise, you will create a program that removes all of the comments from a
Python source file. Check each line in the file to determine if a # character is present.
If it is then your program should remove all of the characters from the # character to
the end of the line (we will ignore the situation where the comment character occurs
inside of a string). Save the modified file using a new name. Both the name of the
input file and the name of the output file should be read from the user. Ensure that an
appropriate error message is displayed if a problem is encountered while accessing
either of the files.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

"""
note that in this exercise file to open must be specified as file_paths
"""

# read and open the input file
try:
    in_name = input('Enter name of a Python file: ')
    inf = open(in_name, 'r')
except:
    print('A problem occured while opening input file')
    quit()

# read and open the output file
try:
    out_name = input('Enter the output file name: ')
    outf = open(out_name, 'w')
except:
    print('A problem occured while opening output file')
    quit()

try:
    # looping each line of the file opened in read mode
    for line in inf:
        # finding the index of character # (if not present it will be -1)
        pos = line.find('#')
    
    # if a comment exists, it will have an index higher than -1
        # in that case the program edits the line by counting all characters until that index (excluded)
        if pos > -1:
            line = line[0 : pos]
            line = line + '\n'
        # adding the line (potentially edited) to the new file
        outf.write(line)

    inf.close()
    outf.close()

except:
    print('Problem while processing the file')

