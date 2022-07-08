"""
Exercise 166: Distinct Names

In this exercise, you will create a program that reads every file in the baby names
data set described in Exercise 163. As your program reads the files, it should keep
track of every distinct name used for a boy and every distinct name used for a girl.
Then your program should output each of these lists of names. Neither of the lists
should contain any repeated values.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

from dict_of_names import dictOfNames
from pathlib import Path

FIRST_YEAR = 1900
LAST_YEAR = 2012

all_girl_names = []
all_boy_names = []

data_folder = Path("files/baby_names/BabyNames/")
first_path_g = data_folder / "1900_GirlsNames.txt"
first_path_b = data_folder / "1900_BoysNames.txt"

# creating a based dictionary built upon files of year 1900
d_girls = dictOfNames(first_path_g)
d_boys = dictOfNames(first_path_b)

# then looping the following years and invoking the function which creates in its turn new dictionaries
# to optimize, the program uses the update method on the base dictionary

try:
    for y in range(FIRST_YEAR, LAST_YEAR + 1):
        variable_path_g = data_folder / (str(y) + "_GirlsNames.txt")
        variable_path_b = data_folder / (str(y) + "_BoysNames.txt")

        # storing the value of the dictionaries built by the function
        # the imported function takes as parameter a file that is specified by a variable path
        variable_d_girls = dictOfNames(variable_path_g)
        variable_d_boys = dictOfNames(variable_path_b)

        # invoke the update method on the base dictionary by passing it the variable dictionary
        d_girls.update(variable_d_girls)
        d_boys.update(variable_d_boys)

except:
    print('Something went wrong: check year range or file path')
    quit()

all_girl_names = list(d_girls)
all_boy_names = list(d_boys)

if __name__ == '__main__':
    print('A total of %d names were used for girls: ' % len(all_girl_names))
    print(all_girl_names)
    print()
    print('A total of %d names were used for boys: ' % len(all_boy_names))
    print(all_boy_names)
