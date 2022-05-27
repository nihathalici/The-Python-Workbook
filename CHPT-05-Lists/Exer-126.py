"""
Exercise 126: Dealing Hands of Cards

In many card games each player is dealt a specific number of cards after the deck
has been shuffled. Write a function, deal, which takes the number of hands, the
number of cards per hand, and a deck of cards as its three parameters. Your function
should return a list containing all of the hands that were dealt. Each hand will be
represented as a list of cards.
When dealing the hands, your function should modify the deck of cards passed
to it as a parameter, removing each card from the deck as it is added to a player’s
hand. When cards are dealt, it is customary to give each player a card before any
player receives an additional card. Your function should follow this custom when
constructing the hands for the players.
Use your solution to Exercise 125 to help you construct a main program that
creates and shuffles a deck of cards, and then deals out four hands of five cards each.
Display all of the hands of cards, along with the cards remaining in the deck after
the hands have been dealt.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

from create_deck import createDeck, shuffle, check_deck

def deal(n_hands, n_cards, deck):
    res = []
    for hand in range(0, n_hands):
        res.append(list())
    
    for c in range(n_cards):
        for h in range(n_hands):
            res[h].append(deck.pop())
    print(res)
    

def main():
    mydeck = createDeck()
    mydeck_shuffle = shuffle(mydeck)
    print(mydeck_shuffle)
    print('The deck has %d cards in total' % len(mydeck_shuffle))
    print()

    print('Here are the hands:')
    deal(4, 5, mydeck_shuffle)
    print('The deck has %d remaining cards' % len(mydeck_shuffle))
    

if __name__ == '__main__':
    main()