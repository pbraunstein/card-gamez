from collections import deque
from random import random

from model.deck import Deck
from model.rank import Rank

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
    while not self.game_over():
        break
        # flip card from whoever is up

        # check if it's a slap. if so evaluate slap, declare winner, give the winner the next turn, reset chances_remaining, and continue the loop

        # now we know it's not a slap

        # put newly flipped card on self.top_card, puth self.top_card to prev_card and prev_card to pile (not in that order though)

        # check if face card, if so reset chances_remaining, flip the turn and continue the loop

        # now we know it's not a face card and not a slap

        # if chances_remaining is not None and chances_remaining == 0, end of turn, move cards over and flip turn, continue loop

        # if chances_remaining is not None and chances_remaining > 0, continue loop, TURN DOES NOT FLIP

        # if chances_remaining is None continue loop flip turn

    def game_over(self):
        return len(self.a_player) == 0 or len(self.b_player) == 0

    def a_won_slap(self):
        return True if random() < self.a_slap_probability else False

    def set_chances_remaining(self):
        """
        When a face card is played, the number of chances remaining needs to
        be set depending on the value of the face card.

        This method assumes that the face card that has already been played
        from which the value is to be set has already been assigned to
        self.top_card.

        This method throws an error if the top_card is not a face card because
        there are no chances remaining when the card is not a face card.
        """
        if not self.top_card.is_face_card():
            raise ValueError(
                    'top_card must be a face card to set chances_remaining')

        if self.top_card.rank == Rank.ACE:
            self.chances_remaining = 4
        elif self.top_card.rank == Rank.KING:
            self.chances_remaining = 3
        elif self.top_card.rank == Rank.QUEEN:
            self.chances_remaining = 2
        elif self.top_card.rank == Rank.JACK:
            self.chances_remaining = 1
        else:
            raise NotImplementedError('THIS SHOULD NEVER HAPPEN')

