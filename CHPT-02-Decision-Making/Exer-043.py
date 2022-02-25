"""
Exercise 43: Frequency to Note

In the previous question you converted from a note’s name to its frequency. In this
question you will write a program that reverses that process. Begin by reading a
frequency from the user. If the frequency is within one Hertz of a value listed in
the table in the previous question then report the name of the corresponding note.
Otherwise report that the frequency does not correspond to a known note. In this
exercise you only need to consider the notes listed in the table. There is no need to
consider notes from other octaves.
"""

# Read a frequency from the user and display the note (if any) that it corresponds to.

C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88
LIMIT = 1

# Read the frequency from the user
freq = float(input("Enter a frequency (Hz): "))

# Determine the note that corresponds to the entered frequency. Set note equal to the empty
# string if there isn’t a match.
if freq >= C4_FREQ - LIMIT and freq <= C4_FREQ + LIMIT:
    note = "C4"
elif freq >= D4_FREQ - LIMIT and freq <= D4_FREQ + LIMIT:
    note = "D4"
elif freq >= E4_FREQ - LIMIT and freq <= E4_FREQ + LIMIT:
    note = "E4"
elif freq >= F4_FREQ - LIMIT and freq <= F4_FREQ + LIMIT:
    note = "F4"
elif freq >= G4_FREQ - LIMIT and freq <= G4_FREQ + LIMIT:
    note = "G4"
elif freq >= A4_FREQ - LIMIT and freq <= A4_FREQ + LIMIT:
    note = "A4"
else:
    note = ""

# Display the result, or an appropriate error message

if note == "":
    print("There is no note that corresponds to that frequency.")
else:
    print("That frequency is ", note)
