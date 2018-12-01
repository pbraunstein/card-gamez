from collections import deque
from random import random

from model.deck import Deck

class Egrt(object):
    def __init__(self, a_slap_probability, deck=None):
        if a_slap_probability < 0 or a_slap_probability >= 1:
            raise ValueError('a_slap_probability must be between 0 and 1')
        self.a_slap_probability = a_slap_probability

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

        # When chances_remaining is None, a player is not responding to
        # the other player's face card. When it becomes 0, the
        # player responding to the face card has lost the hand
        # and chances_remaining should be reset to None.
        self.chances_remaining = None

    def simulate_game(self, debug_print=False):
        pass

    def game_over(self):
        return len(self.a_player) == 0 or len(self.b_player) == 0

    def a_won_slap(self):
        return True if random() < self.a_slap_probability else False
