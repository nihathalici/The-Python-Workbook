"""
Exercise 164: Gender Neutral Names

Some names, like Ben, Jonathan and Andrew are normally only used for boys while
names like Rebecca and Flora are normally only used for girls. Other names, like
Chris and Alex, may be used for both boys and girls.
Write a program that determines and displays all of the baby names that were used
for both boys and girls in a year specified by the user. Your program should generate
an appropriate message if there were no gender neutral names in the selected year.
Display an appropriate error message if you do not have data for the year requested
by the user.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

import os.path

# the following function is used to store all names of a given file as keys of a given dictionary
# function is invoked, for a specific year, both for boys and girls files, that will be then compared
# if among the two dictionary there is a corresponding key, that key is a gender neutral name

def dictOfNames(fname):
    d = {}
    inf = open(fname, 'r')
    for line in inf:
        parts = line.split()
        name = parts[0]
        d[name] = ""  # otherwise None
    return d

def main():
    year = input('Enter a year between 1900 and 2012: ')
    try:
        data_folder = os.path.join("files", "baby_names", "BabyNames", str(year))
        girl_fname = data_folder + "_GirlsNames.txt"
        boy_fname = data_folder + "_BoysNames.txt"

        girl_names = dictOfNames(girl_fname)
        boy_names = dictOfNames(boy_fname)

        neutrals = []
        for k in girl_names:
            if k in boy_names:
                neutrals.append(k)
        
        if neutrals != []:
            for name in neutrals:
                print(name, end='  ')
        else:
            print('No gender neutral names in that specific year')
    except:
        print('Please enter a valid year')

if __name__ == '__main__':
    main()