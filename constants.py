from enum import Enum, IntEnum, auto,  unique

@unique
class Suit(Enum):
    SPADE = auto()
    CLUB = auto()
    HEART = auto()
    DIAMOND = auto()

@unique
class Rank(IntEnum):
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

