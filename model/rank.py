from enum import IntEnum, unique

from model.model_constants import TYPE_ERROR_MESSAGE, THIS_SHOULD_NEVER_HAPPEN

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

    # Normally __ne__ automatically delegates to __eq__ making it unnecessary
    # However, because IntEnum inherits from integer which has a __ne__
    # definition, __ne__ delegates to the int's __ne__ which doesn't do the
    # type checking required here. Because of this, I've implemented an __ne__
    def __ne__(self, other):
        return not self.__eq__(other)

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

    def __str__(self):
        if self == Rank.TWO:
            return 'two'
        elif self == Rank.THREE:
            return 'three'
        elif self == Rank.FOUR:
            return 'four'
        elif self == Rank.FIVE:
            return 'five'
        elif self == Rank.SIX:
            return 'six'
        elif self == Rank.SEVEN:
            return 'seven'
        elif self == Rank.EIGHT:
            return 'eight'
        elif self == Rank.NINE:
            return 'nine'
        elif self == Rank.TEN:
            return 'ten'
        elif self == Rank.JACK:
            return 'jack'
        elif self == Rank.QUEEN:
            return 'queen'
        elif self == Rank.KING:
            return 'king'
        elif self == Rank.ACE:
            return 'ace'
        else:
            raise NotImplementedError(THIS_SHOULD_NEVER_HAPPEN)

    def __repr__(self):
        return self.__str__()

