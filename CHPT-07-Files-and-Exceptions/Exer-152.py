"""
Exercise 152: Number the Lines in a File

Create a program that reads lines from a file, adds line numbers to them, and then
stores the numbered lines into a new file. The name of the input file will be read from
the user, as will the name of the new file that your program will create. Each line in
the output file should begin with the line number, followed by a colon and a space,
followed by the line from the input file.
"""

from pathlib import Path

data_folder = Path("files")
file_to_read = data_folder / 'sonnet.txt'
file_to_create = data_folder / 'sonnet_numbered.txt'

fin1 = open(file_to_read, 'r')
fin2 = open(file_to_create, 'w')
# mode 'w' overwrites the content, if the file exists, otherwise it creates a new file with that content
# instead, if I used mode 'a', the content would be added to the end of the file
# if the file that I want to edit is empty, it does not change anything between 'w' and 'a'

i = 1

for x in fin1:
    fin2.write("%d: %s" % (i, x))
    i += 1

fin1.close()
fin2.close()

display = open('sonnet_numbered.txt', 'r')

for num_line in display:
    num_line = num_line.rstrip()
    print(num_line)

"""or
for el in display.readlines():
    print(el.rstrip())
"""

display.close()