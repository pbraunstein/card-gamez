from model.model_constants import TYPE_ERROR_MESSAGE
from model.suit import Suit
from model.rank import Rank

class Card(object):
    def __init__(self, rank, suit):
        # Enforce typing
        if not isinstance(rank, Rank):
            raise TypeError('rank must be of type Rank')
        if not isinstance(suit, Suit):
            raise TypeError('suit must be of type Suit')
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return '{} of {}s'.format(
                repr(self.rank).title(),
                repr(self.suit).title())

    def __repr__(self):
        return self.__str__()

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit
