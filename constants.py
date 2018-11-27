from enum import Enum, IntEnum, auto,  unique

TYPE_ERROR_MESSAGE = 'A {} is not comparable to a {}'

# TODO Split Suit and Enums out other files

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

@unique
class Rank(IntEnum):
    """
    Rank values are comparable. Even though it should not matter,
    each Rank is assigned to its semantic value (i.e. TWO maps to 2 not 0).

    Raises TypeError if compared to a different type. This is to prevent
    abuses of the enum (even though Rank.TWO == 2 would be correct withou
    this, it defeats the purpose of using an enum).
    """
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
    ACE = 14

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return super().__eq__(other)
        else:
            raise TypeError(TYPE_ERROR_MESSAGE.format(
                self.__class__,
                other.__class__))

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return super().__lt__(other)
        else:
            raise TypeError(TYPE_ERROR_MESSAGE.format(
                self.__class__,
                other.__class__))

    def __le__(self, other):
        if self.__class__ == other.__class__:
            return super().__le__(other)
        else:
            raise TypeError(TYPE_ERROR_MESSAGE.format(
                self.__class__,
                other.__class__))
        
    def __gt__(self, other):
        if self.__class__ == other.__class__:
            return super().__gt__(other)
        else:
            raise TypeError(TYPE_ERROR_MESSAGE.format(
                self.__class__,
                other.__class__))

    def __ge__(self, other):
        if self.__class__ == other.__class__:
            return super().__ge__(other)
        else:
            raise TypeError(TYPE_ERROR_MESSAGE.format(
                self.__class__,
                other.__class__))
