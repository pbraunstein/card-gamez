from enum import Enum, auto, unique

from constants import TYPE_ERROR_MESSAGE

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
