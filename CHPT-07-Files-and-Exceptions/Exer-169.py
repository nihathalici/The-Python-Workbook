"""
Exercise 169: Redacting Text in a File

Sensitive information is often removed, or redacted, from documents before they
are released to the public. When the documents are released it is common for the
redacted text to be replaced with black bars.
In this exercise you will write a program that redacts all occurrences of sensitive
words in a text file by replacing them with asterisks. Your program should redact
sensitive words wherever they occur, even if they occur in the middle of another
word. The list of sensitive words will be provided in a separate text file. Save the
redacted version of the original text in a new file. The names of the original text file,
sensitive words file, and redacted file will all be provided by the user.
"""
# Author's solution
##
# Redact a text file by removing all occurrences of sensitive words. The redacted version
# of the text is written to a new file.
#
# Note that this program does not perform any error checking, and it does not implement
# case insensitive redaction.
#
# Get the name of the input file and open it
inf_name = input("Enter the name of the text file to redact: ")
inf = open(inf_name, "r")

# Get the name of the sensitive words file and open it
sen_name = input("Enter the name of the sensitive words file: ")
sen = open(sen_name, "r")

# Load all of the sensitive words into a list
words = []
line = sen.readline()
while line != "":
    line = line.rstrip()
    words.append(line)
    line = sen.readline()

# Close the sensitive words file
sen.close()

"""
The sensitive word file can be closed at this point because all of the words have been read
into a list. No further data needs to be read from that file.
"""

# Get the name of the output file and open it
outf_name = input("Enter the name for the new redacted file: ")
outf = open(outf_name, "w")

# Read each line from the input file. Replace all of the sensitive words with asterisks. Then
# write the line to the output file.
line = inf.readline()
while line != "":
    # Check for and replace each sensitive word. The number of asterisks matches the number
    # of letters in the word being redacted.
    for word in words:
        line = line.replace(word, "*" * len(word))
    
    # Write the modified line to the output file
    outf.write(line)

    # Read the next line from the input file
    line = inf.readline()
# Close the input and output files
inf.close()
outf.close()