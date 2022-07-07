"""
Exercise 165: Most Births in a given Time Period

Write a program that uses the baby names data set described in Exercise 163 to
determine which names were used most often within a time period. Have the user
supply the first and last years of the range to analyze. Display the boy’s name and
the girl’s name given to the most children during the indicated years.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

import os.path

year1 = input('Enter the starting year: ')
year2 = input('Enter the closing year: ')

data_folder = os.path.join('files', 'baby_names', 'BabyNames')
girl_names = []
boy_names = []

for y in range(int(year1), int(year2) + 1):
    file_to_open_g = os.path.join(data_folder, f"{y}_GirlsNames.txt")
    file_to_open_b = os.path.join(data_folder, f"{y}_BoysNames.txt")

    girl_fname = open(file_to_open_g, 'r')
    boy_fname = open(file_to_open_b, 'r')

    girl_name = girl_fname.readline().split()[0]
    boy_name = boy_fname.readline().split()[0]

    if girl_name not in girl_names:
        girl_names.append(girl_name)
    if boy_name not in boy_names:
        boy_names.append(boy_name)

def main():
    print(f"Here are the most common girl names between {year1} and {year2}: ")
    for name in girl_names:
        print(name, end='  ')
    
    print()

    print(f"Here are the most common boy names between {year1} and {year2}: ")
    for name in boy_names:
        print(name, end='  ')

if __name__ == '__main__':
    main()
