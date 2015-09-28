from collections import deque
from enum import Enum
from random import shuffle

class Suit(Enum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3
    
class Value(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Card:
    def __init__(self, suit, value):
        if isinstance(suit,Suit):
            self.suit = suit
        else:
            raise Error("not a suit")
        if isinstance(value,Value):
            self.value = value
        else:
            raise Error("not a value")
    def __str__(self):
        return self.value.name + " of " + self.suit.name
    
class Deck:
    def __init__(self,shuffled=True):
        self.deck = deque()
        for i in range(1,14):
            for j in range(4):
                self.deck.append(Card(Suit(j),Value(i)))
        if shuffled:
            shuffle(self.deck)
    def next(self):
        return self.deck.pop()
    def size(self):
        return len(self.deck)

class Player:
    def __init__(self):
        self.deck = deque()
    def dealt(self,card):
        self.deck.appendleft(card)
    def pickUp(self, cards):
        self.deck.extendleft(cards)
    def next(self):
        return self.deck.pop()
        
