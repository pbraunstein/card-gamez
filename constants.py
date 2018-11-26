from enum import Enum, auto,  unique

@unique
class Suit(Enum):
    SPADE = auto()
    CLUB = auto()
    HEART = auto()
    DIAMOND = auto()

