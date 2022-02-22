"""
Exercise 40: Sound Levels

The following table lists the sound level in decibels for several common noises.
  ____________________________
  Noise          Decibel Level
  ----------------------------
  Jackhammer        130 dB
  Gas Lawnmower     106 dB
  Alarm Clock        70 dB
  Quiet Room         40 dB 

Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the value is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

dbLevel = float(input("Please enter a dB level: "))

# Handle the quietest and loudest noises
if dbLevel < 40:
	print("This is extremely quite.")
elif dbLevel > 130:
	print("This is extremely loud.")
	

# In-between noises	
if dbLevel > 40:
	print("This is between a quiet room and an alram clock.")
elif dbLevel > 70:
	print("This is between an alarm clock and a gas lawnmower.")
elif dbLevel > 106:
	print("This is between a gas lawnmower and a jackhammer.")

# Matching noises	
if dbLevel == 40:
	print("This is a quiet room.")
elif dbLevel == 70:
	print("This is an alarm clock.")
elif dbLevel == 106:
	print("This is a gas lawnmower.")
elif dbLevel == 130:
	print("This is a jackhammer.")
