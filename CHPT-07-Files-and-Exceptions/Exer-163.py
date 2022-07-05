"""
Exercise 163: Names that Reached Number One

The baby names data set consists of over 200 files. Each file contains a list of 100
names, along with the number of times each name was used. Entries in the files are
ordered from most frequently used to least frequently used. There are two files for
each year: one containing names used for girls and the other containing names used
for boys. The data set includes data for every year from 1900 to 2012.

Write a program that reads every file in the data set and identifies all of the names
that were most popular in at least one year. Your program should output two lists:
one containing the most popular names for boys and the other containing the most
popular names for girls. Neither of your lists should include any repeated values.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

from pathlib import Path

FIRST_YEAR = 1900
LAST_YEAR = 2012

def LoadAndAdd(fname, names):
    inf = open(fname, 'r')
    line = inf.readline()
    inf.close()
    parts = line.split()
    name = parts[0]
    if name not in names:
        names.append(name)

def main():
    girls = []
    boys = []

    data_folder = Path("files/baby_names/BabyNames/")

    for year in range(FIRST_YEAR, LAST_YEAR + 1):
        f_to_open_g = data_folder / (str(year) + "_GirlsNames.txt")
        f_to_open_b = data_folder / (str(year) + "_BoysNames.txt")
        LoadAndAdd(f_to_open_g, girls)
        LoadAndAdd(f_to_open_b, boys)

    print('Girls\' names that reached #1:')
    for name in girls:
        print(' ', name)
    print()
    print('Boys\' names that reached #1:')
    for name in boys:
        print(' ', name)

if __name__  == '__main__':
    main()
