"""
Exercise 73: Caesar Cipher

One of the first known examples of encryption was used by Julius Caesar. Caesar
needed to provide written instructions to his generals, but he didn’t want his enemies
to learn his plans if the message slipped into their hands. As a result, he developed
what later became known as the Caesar cipher.
The idea behind this cipher is simple (and as such, it provides no protection against
modern code breaking techniques). Each letter in the original message is shifted by
3 places. As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc.
The last three letters in the alphabet are wrapped around to the beginning: X becomes
A, Y becomes B and Z becomes C. Non-letter characters are not modified by the
cipher.
Write a program that implements a Caesar cipher. Allow the user to supply the
message and the shift amount, and then display the shifted message. Ensure that
your program encodes both uppercase and lowercase letters. Your program should
also support negative shift values so that it can be used both to encode messages and
decode messages.
"""
# Author's solution
##
# Implement a Caesar cipher that shifts all of the letters in a message by an amount provided
# by the user. Use a negative shift value to decode a message.
#
# Read the message and shift amount from the user
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Process each character to construct the encrypted (or decrypted) message
new_message = ""
for ch in message:
    if ch >= "a" and ch <= "z":
        # Process a lowercase letter by determining its
        # position in the alphabet (0 - 25), computing its
        # new position, and adding it to the new message
        # The ord function converts a character to its
        # teger position within the ASCII table
        pos = ord(ch) - ord("a")
        pos = (pos + shift) % 26
        new_char = chr(pos + ord("a"))
        new_message = new_message + new_char
    elif ch >= "A" and ch <= "Z":
        # Process an uppercase letter by determining its position in the alphabet (0 - 25),
        # computing its new position, and adding it to the new message
        pos = ord(ch) - ord("A")
        pos = (pos + shift) % 26
        new_char = chr(pos + ord("A"))
        new_message = new_message + new_char
    else:
        # If the character is not a letter then copy it into the new message
        new_message = new_message + ch

# Display the shifted message
print("The shifted message is", new_message)

