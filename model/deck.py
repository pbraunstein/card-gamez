from model.card import Card

class Deck(object):
    def __init__(self):
        self._dealt = False


    @property
    def dealt(self):
        return self._dealt
