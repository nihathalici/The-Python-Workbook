"""
Exercise 84: Coin Flip Simulation

What’s the minimum number of times you have to flip a coin before you can have
three consecutive flips that result in the same outcome (either all three are heads or
all three are tails)? What’s the maximum number of flips that might be needed? How
many flips are needed on average? In this exercise we will explore these questions
by creating a program that simulates several series of coin flips.

Create a program that uses Python’s random number generator to simulate flipping
a coin several times. The simulated coin should be fair, meaning that the probability
of heads is equal to the probability of tails. Your program should flip simulated
coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each
time the outcome is heads, and a T each time the outcome is tails, with all of the
outcomes for one simulation on the same line. Then display the number of flips that
were needed to reach 3 consecutive occurrences of the same outcome. When your
program is run it should perform the simulation 10 time

H T T T (4 flips)
H H T T H T H T T H H
T T T (3 flips)
T H H H (4 flips)
H H H (3 flips)
T H T T H T H H T T H
H T T H H H (6 flips)
T H T T T (5 flips)
T T H T T H T H T H H
T H T T T (5 flips)
On average, 7.9 flips
57
T H T T H T T T (19 flips)
H T H T H H H (18 flips)
H (12 flips)
were needed.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

import random 

def coin_flip():
    rep_H = 0
    rep_T = 0
    flips = 0
    sequence = ''
    while rep_H < 3 and rep_T < 3:
        side = random.randint(1,2)
        flips += 1
        if side == 1:
            rep_H += 1
            rep_T = 0
            sequence += ' H'
        elif side == 2:
            rep_T += 1
            rep_H = 0
            sequence += ' T'
        if rep_H == 3 or rep_T == 3:
            print(sequence, '(%d flips)' % flips)
            return flips

num_of_simulations = 10
tot_flips = 0

for i in range(num_of_simulations):
    tot_flips += coin_flip()

average_flips = tot_flips / num_of_simulations
print('On average, %.1f flips were needed in order to encounter three consecutive equal H or T' % average_flips)
