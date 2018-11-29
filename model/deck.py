from random import shuffle

from model.card import Card
from model.model_constants import DoubleDealtDeckError
from model.rank import Rank
from model.suit import Suit

class Deck(object):
    """
    Represents a standard 52 card deck (no jokers / special cards).

    Each Deck instance may only be dealt a single time otherwise an error gets
    raised. This is to guard against multiple games pointing to the same Card
    at the same time. (I'm not convinced this would cause problems,
    but I'm also not convinced it wouldn't cause problems.
    """
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
