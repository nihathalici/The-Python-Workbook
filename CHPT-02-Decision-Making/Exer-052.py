"""
Exercise 52: Letter Grade to Grade Points

At a particular university, letter grades are mapped to grade points in the following
manner:

---------------------
Letter  Grade Points
---------------------

A+      4.0         
A       4.0
A-      3.7
B+      3.3
B       3.0
B-      2.7
C+      2.3
C       2.0
C-      1.7
D+      1.3
D       1.0
F       0
---------------------

Write a program that begins by reading a letter grade from the user. Then your
program should compute and display the equivalent number of grade points. Ensure
that your program generates an appropriate error message if the user enters an invalid
letter grade.
"""
# Author's solution:
# Convert from a letter grade to a number of grade points.

A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0
INVALID = -1

# Read the letter grade from the user
letter = input("Enter a letter grade: ")
letter = letter.upper()

# Convert from a letter grade to a number of grade points
# using -1 grade points as a sentinel value indicating invalid input
if letter == "A+" or letter == "A":
        gp = A
elif letter == "A-":
        gp = A_MINUS
elif letter == "B+":
        gp = B_PLUS
elif letter == "B":
        gp = B
elif letter == "B-":
        gp = B_MINUS
elif letter == "C+":
        gp = C_PLUS
elif letter == "C":
        gp = C
elif letter == "C-":
        gp = C_MINUS
elif letter == "D+":
        gp = D_PLUS
elif letter == "D":
        gp = D
elif letter == "F":
        gp = F
else:
        gp = INVALID

# Report the result
if gp == INVALID:
    print("That wasn’t a valid letter grade.")
else:
    print("A(n)", letter, "is equal to", gp, "grade points.")
        
        


