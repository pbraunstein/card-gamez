from collections import deque
from random import random
from time import sleep

from model.deck import Deck
from model.rank import Rank

SLEEP_DELAY = 2

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

        hand_1, hand_2 = self.deck.deal()
        self.a_player = deque(hand_1)
        self.b_player = deque(hand_2)

        self.a_turn = True  # the A player always goes first

        # When chances_remaining is None, a player is not responding to
        # the other player's face card. When it becomes 0, the
        # player responding to the face card has lost the hand
        # and chances_remaining should be reset to None.
        self.chances_remaining = None

        self.counter = 0

    def simulate_game(self, debug_print=False):
        while not self.game_over():
            self.counter += 1
            if debug_print:
                sleep(SLEEP_DELAY)
                print()
                print('turn: {}'.format(self.counter))
                print('A: {}, B: {}, pile: {}'.format(
                    len(self.a_player), len(self.b_player), self.pile_size()))
            if self.a_turn:
                new_card = self.a_player.popleft()
                if debug_print:
                    print('A plays {}'.format(new_card))
            else:
                new_card = self.b_player.popleft()
                if debug_print:
                    print('B plays {}'.format(new_card))

            # Need to check if a slap happened before pushing new_card to
            # top_card so that it is possible to check for sandwiches.
            slap_happened = self.is_slap(new_card)

            # Push prev_card to pile, top_card to prev_card, and new_card
            # to top_card
            if self.prev_card is not None:
                self.pile.append(self.prev_card)
            if self.top_card is not None:
                self.prev_card = self.top_card
            self.top_card = new_card

            if slap_happened:
                if self.a_won_slap():
                    if debug_print:
                        sleep(SLEEP_DELAY)
                        print('A wins slap')
                    self.add_cards_to_hand(self.a_player)
                    self.a_turn = True
                else:
                    if debug_print:
                        sleep(SLEEP_DELAY)
                        print('B wins slap')
                    self.add_cards_to_hand(self.b_player)
                    self.a_turn = False
                continue

            if self.top_card.is_face_card():
                self.set_chances_remaining()
                self.a_turn = not self.a_turn
                continue

            if self.chances_remaining is None:
                self.a_turn = not self.a_turn
                continue

            self.chances_remaining -= 1

            # Whichever player is up just ran out of turns
            if self.chances_remaining == 0:
                # If a just lost the turn, add the cards to b
                if self.a_turn:
                    self.add_cards_to_hand(self.b_player)
                    if debug_print:
                        sleep(SLEEP_DELAY)
                        print('B wins hand')
                else:  # if b just lost the turn, add cards to a
                    self.add_cards_to_hand(self.a_player)
                    if debug_print:
                        sleep(SLEEP_DELAY)
                        print('A wins hand')
                self.a_turn = not self.a_turn

        if len(self.a_player) == 0 and len(self.b_player) == 0:
            victor = 'T'
        elif len(self.b_player) == 0:
            victor = 'A'
        else:
            victor = 'B'

        return victor, self.counter


    def game_over(self):
        return len(self.a_player) == 0 or len(self.b_player) == 0

    def is_slap(self, new_card):
        # Can't be a slap if it is the first card in the pile
        if self.top_card is None:
            return False

        # check classic slap
        if self.top_card == new_card:
            return True

        # check Queen / King slap
        if (self.top_card.rank == Rank.QUEEN and new_card.rank == Rank.KING or
                self.top_card.rank == Rank.KING and new_card.rank == Rank.QUEEN):
            return True

        # check sandwich slap
        if self.prev_card is not None and self.prev_card == new_card:
            return True
        else:
            return False

    def a_won_slap(self):
        return True if random() < self.a_slap_probability else False

    def add_cards_to_hand(self, hand):
        if self.top_card is None or self.prev_card is None:
            raise ValueError(
                    'Must be at least two cards to call add_cards_to_hand')

        hand.extend(self.pile)
        hand.append(self.prev_card)
        hand.append(self.top_card)

        self.pile.clear()
        self.prev_card = None
        self.top_card = None
        self.chances_remaining = None

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

    def pile_size(self):
        size = 0
        if self.top_card is not None:
            size += 1
        if self.prev_card is not None:
            size += 1
        return size + len(self.pile)

