from enum import Enum, auto, unique

from model.model_constants import TYPE_ERROR_MESSAGE, THIS_SHOULD_NEVER_HAPPEN

@unique
class Suit(Enum):
    """
    Suit values support equality but not order comparisons.

    A TypeError is raised if an equality operator is used with a
    value of another type.
    """
    SPADE = auto()
    CLUB = auto()
    HEART = auto()
    DIAMOND = auto()

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return super().__eq__(other)
        else:
            raise TypeError(TYPE_ERROR_MESSAGE.format(
                self.__class__,
                other.__class__))

    def __str__(self):
        if self == Suit.SPADE:
            return 'spade'
        elif self == Suit.CLUB:
            return 'club'
        elif self == Suit.HEART:
            return 'heart'
        elif self == Suit.DIAMOND:
            return 'diamond'
        else:
            raise NotImplementedError(THIS_SHOULD_NEVER_HAPPEN)

    def __repr__(self):
        return self.__str__()
