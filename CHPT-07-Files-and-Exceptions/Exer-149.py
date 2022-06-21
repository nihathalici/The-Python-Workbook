"""
Exercise 149: Display the Head of a File

Unix-based operating systems usually include a tool named head. It displays the
first 10 lines of a file whose name is provided as a command line argument. Write
a Python program that provides the same behaviour. Display an appropriate error
message if the file requested by the user does not exist, or if the command line
argument is omitted.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

from pathlib import Path

data_folder = Path("files")
file_to_open = data_folder / "lines.txt"

fin = open(file_to_open, 'r')
for i in range(10):
    print(fin.readline())

