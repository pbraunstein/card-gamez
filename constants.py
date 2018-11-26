from enum import Enum, IntEnum, auto,  unique

@unique
class Suit(Enum):
    """ Suit values are not orderable. """
    SPADE = auto()
    CLUB = auto()
    HEART = auto()
    DIAMOND = auto()

@unique
class Rank(IntEnum):
    """
    Rank values are comparable. Even though it should not matter if
    used correctly (i.e. only compared to other Ranks), the value of each
    Rank is set to its semantic value.
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

