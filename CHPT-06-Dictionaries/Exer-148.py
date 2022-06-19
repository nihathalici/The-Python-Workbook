"""
Exercise 148: Play Bingo

In this exercise you will write a program that simulates a game of Bingo for a single
card. Begin by generating a list of all of the valid Bingo calls (B1 through O75).
Once the list has been created you can randomize the order of its elements by calling
the shuffle function in the random module. Then your program should consume
calls out of the list and cross out numbers on the card until the card contains a winning
line. Simulate 1,000 games and report the minimum, maximum and average number
of calls that must be made before the card wins. You may find it helpful to import
your solutions to Exercises 146 and 147 when completing this exercise.

"""

# Solution by Aldo Telese
# https://github.com/aldotele


from create_bingo_card import bingo_cards, display_bingo_cards
from winning_bingo_card import winning_card

from random import shuffle
import copy


def play_bingo(card):
    # list of all values between 1 and 75, to be shuffled
    all_values = []
    for i in range(1, 76):
        all_values.append(i)
    shuffle(all_values)

    playcard = copy.deepcopy(card)
    call = 0

    while all_values != []:
        value = all_values.pop()
        call += 1
        for seq in playcard:
            for i in range(5):
                if playcard[seq][i] == value:
                    playcard[seq][i] = 0
                    break
            # if entering another break here, it would not check other seq in case the value is not in the first one
        if winning_card(playcard):
            return call


# BINGO IN DISPLAY MODE
def play_bingo_display_mode(card):
    all_values = []
    for i in range(1, 76):
        all_values.append(i)
    shuffle(all_values)

    playcard = copy.deepcopy(card)
    call = 0
    while all_values != []:
        value = all_values.pop()
        call += 1
        print()
        print('call number %d: the extracted number is %d' % (call, value))
        for seq in playcard:
            for i in range(5):
                if playcard[seq][i] == value:
                    playcard[seq][i] = 0
                    # display_bingo_cards(playcard)
                    break
        if winning_card(playcard):
            print()
            print('you WON at call %d!. Last number called was %d' % (call, value))
            display_bingo_cards(playcard)
            return call


# following function simulates a bingo foor 1000 times on the same card, extracting data
def play_1000_bingo(card):
    # list with all calls that are necessary to end each of the 1000 bingos
    calls = []
    thecard = bingo_cards()
    for i in range(1000):
        call = play_bingo(thecard)
        calls.append(call)
    highest_call = max(calls)
    lowest_call = min(calls)
    avg_call = sum(calls) / 1000
    print('highest call: %d' % highest_call)
    print('lowest call: %d' % lowest_call)
    print('average call: %.1f' % avg_call)


def main():
    # create a card, print it and simulate 1000 times a bingo on the same card
    # this is done to analyze data about max, min and avg call
    mycard = bingo_cards()
    print(mycard)
    play_1000_bingo(mycard)


if __name__ == '__main__':
    main()