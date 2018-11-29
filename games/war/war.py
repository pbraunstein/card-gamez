from model.deck import Deck

class War(object):
    def __init__(self, deck=None):
        if deck is None:
            self.deck = Deck()
        else:
            if isinstance(deck, Deck):
                self.deck = deck
            else:
                raise TypeError('deck must be of type Deck')
