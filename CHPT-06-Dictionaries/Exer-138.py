"""
Exercise 138: Text Messaging

On some basic cell phones, text messages can be sent using the numeric keypad.
Because each key has multiple letters associated with it, multiple key presses are
needed for most letters. Pressing the number once generates the first character listed
for that key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth
or fifth character.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

"""
ord('A') = 65
ord('Z') = 90
"""

d = {'.': 1, ',': 11, '?': 111, '!': 1111, ':': 11111, 'A': 2, 'B': 22, 'C': 222, 'D': 3, 'E': 33, 'F': 333, 'G': 4,
     'H': 44, 'I': 444, 'J': 5, 'K': 55, 'L': 555, 'M': 6, 'N': 66,
     'O': 666, 'P': 7, 'Q': 77, 'R': 777, 'S': 7777, 'T': 8, 'U': 88, 'V': 888, 'W': 9, 'X': 99, 'Y': 999, 'Z': 9999,
     ' ': 0}

message = input('Enter message: ')
message = message.upper()
key_message = ''

for c in message:
    key = str(d[c])
    key_message += key

print(key_message)