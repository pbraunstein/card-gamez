from random import shuffle

from model.card import Card
from model.rank import Rank
from model.suit import Suit

class Deck(object):
    def __init__(self):
        self.cards = []
        for rank in Rank:
            for suit in Suit:
                self.cards.append(Card(rank, suit))
        self._dealt = False

    @property
    def dealt(self):
        return self._dealt

    @dealt.setter
    def dealt(self, value):
        self._dealt = value

    def deal(self):
        pass
