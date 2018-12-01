from collections import deque
from random import random

from model.deck import Deck

class Egrt(object):
    def __init__(self, deck=None):
        if deck is None:
            self.deck = Deck()
        else:
            if isinstance(deck, Deck):
                self.deck = deck
            else:
                raise TypeError('deck must be of type Deck')
        
        self.top_card = None
        self.prev_card = None
        self.pile = deque()
        self.a_player = deque()
        self.b_player = deque()

        self.a_turn = True  # the A player always goes first


    def simulate_game(self, debug_print=False):
        pass

    def game_over(self):
        return len(self.a_player) == 0 or len(self.b_player) == 0
