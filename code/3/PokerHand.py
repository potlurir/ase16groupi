"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *

RANKING = {
    "FiveOfAKind" : 1,
    "StraightFlush": 2,
    "FourOfAKind": 3,
    "FullHouse": 4,
    "Flush": 5,
    "Straight": 6,
    "ThreeOfAKind": 7,
    "TwoPair": 8,
    "OnePair": 9,
    "HighCard": 10
}


class PokerHand(Hand):

    def initialize(self):
        self.suitInfoForCardsInHand()
        self.rankInfoForCardsInHand()

    def suitInfoForCardsInHand(self):
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rankInfoForCardsInHand(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_n_pair(self, n):
        values = self.ranks.values()
        return True if sum(1 for val in values if val == 2) == n else False

    def has_n_of_a_kind(self, n):
        values = self.ranks.values()
        return True if sum(1 for val in values if val == n) > 0 else False

    def has_straight(self, n):
        keys = self.ranks.keys()
        keys.sort()
        count = 0
        for i in xrange(len(keys) - 1):
            if keys[i] + 1 == keys[i+1]:
                count += 1
            else:
                count = 0
        if count >= n:
            return True
        return False

    def has_flush(self):
        pass

    def has_full_house(self):
        pass

    def has_four_of_a_kind(self):
        pass

    def has_straight_flush(self):
        pass

    def classify(self):
        if self.has_n_of_a_kind(5):
            self.label = ""


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        hand.initialize()
        print hand
        print "Has Pair: " + str(hand.has_n_pair(1))
        print "Has Two Pairs: " + str(hand.has_n_pair(2))
        print "Has Three of a kind: " + str(hand.has_n_of_a_kind(3))
        print "Has Four of a kind: " + str(hand.has_n_of_a_kind(4))
        print "Has 5 Straight: " + str(hand.has_straight(5))
        print "Has 7 Straight: " + str(hand.has_straight(7))
        print ''
