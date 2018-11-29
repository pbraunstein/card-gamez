from random import shuffle

from model.card import Card
from model.model_constants import DoubleDealtDeckError
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
        if self.dealt:
            raise DoubleDealtDeckError('This deck has already been dealt')
        else:
            self.dealt = True

        shuffle(self.cards)
        return self.cards[::2], self.cards[1::2]
