"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
from __future__ import division

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
        """
            Holds all suits and their respective counts.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rankInfoForCardsInHand(self):
        """
            Holds all ranks and their respective counts.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_n_pair(self, n):
        """
            returns True when number of pairs = n,
            n is the argument passed, else False.
        """
        return True if sum(1 for val in self.ranks.values()
                           if val == 2) == n else False

    def has_n_of_a_kind(self, n):
        """
            returns True when count of certain rank = n,
            n is the argument passed, else False.
        """
        return True if n in self.ranks.values() else False

    # Unfortunately solution was also the same.
    def has_straight(self):
        """
            returns True when 5 contiguous ranks are available,
            else False.
        """
        count = 0
        for i in range(1, 15):
            if i in self.ranks:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
        return False

    def has_flush(self):
        """
            returns True when 5 cards with same suit are available,
            else False.
        """
        return True if 5 in self.suits.values() else False

    def has_full_house(self):
        """
            returns True when hand contains a three and two pair,
            else False.
        """
        return True if self.has_n_pair(2) and self.has_n_of_a_kind(3) else False

    def has_straight_flush(self):
        """
            returns True when hand contains 5 cards with same suit and
            are contiguous, else False.
        """
        self.cards.sort()
        count = 0
        currentSuit = None
        currentRank = None
        for card in self.cards:
            if currentSuit and currentSuit == card.suit and \
                    currentRank and currentRank == card.rank - 1:
                count += 1
                if count == 5: return True
            else:
                count = 0
            currentSuit = card.suit
            currentRank = card.rank
        return False

    def classify(self):
        if self.has_straight_flush():
            self.label = "StraightFlush"
        elif self.has_n_of_a_kind(4):
            self.label = "FourOfAKind"
        elif self.has_full_house():
            self.label = "FullHouse"
        elif self.has_flush():
            self.label = "Flush"
        elif self.has_straight():
            self.label = "Straight"
        elif self.has_n_of_a_kind(3):
            self.label = "ThreeOfAKind"
        elif self.has_n_pair(2):
            self.label = "TwoPair"
        elif self.has_n_pair(1):
            self.label = "OnePair"
        else:
            self.label = "HighCard"
        


if __name__ == '__main__':
    sample = 10000
    labels = {}
    for x in xrange(sample):
        deck = Deck()
        deck.shuffle()
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        hand.initialize()
        hand.classify()
        labels[hand.label] = labels.get(hand.label, 0) + 1
        print hand
        print hand.label
        print ''
    for label, count in labels.iteritems():
        probability = count/sample
        print "Probability of " + label + " is: " + str(probability)