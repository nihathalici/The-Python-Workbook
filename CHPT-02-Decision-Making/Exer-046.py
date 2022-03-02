"""
Exercise 46: What Color Is That Square?

Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row, as shown below:

Write a program that reads a position from the user. Use an if statement to
determine if the column begins with a black square or a white square. Then use
modular arithmetic to report the color of the square in that row. For example, if the
user enters a1 then your program should report that the square is black. If the user
enters d5 then your program should report that the square is white. Your program
may assume that a valid position will always be entered. It does not need to perform
any error checking.
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

gridPos = input("Please enter a chess board position: ")

col = gridPos[0].lower()
row = int(gridPos[1])

if col in "aceg":
    colStartsWithBlack = True
else:
    colStartsWithBlack = False

if colStartsWithBlack:
    if row % 2 == 0:
        white = True
    else:
        white = False
else:
    if row % 2 == 0:
        white = False
    else:
        white = True

if white:
    print("That position is coloured white.")
else:
    print("That position is coloured black.")

