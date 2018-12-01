from collections import deque
from random import randint
from time import sleep

from model.deck import Deck

class War(object):
    """
    Simulates a game of war. The order in which the players' cards stack in
    each hand is nondeterministic.

    The game is over when either of the players runs out of cards. This is the
    case even if there are left over cards (e.g. the last card a player puts
    down results in a tie).
    """
    def __init__(self, deck=None):
        if deck is None:
            self.deck = Deck()
        else:
            if isinstance(deck, Deck):
                self.deck = deck
            else:
                raise TypeError('deck must be of type Deck')

        hand_1, hand_2 = self.deck.deal()
        self.a_player = deque(hand_1)
        self.b_player = deque(hand_2)
        self.pile = deque()
        self.counter = 0

    def simulate_game(self, debug_print=False):
        while not self.game_over():
            a_card = self.a_player.popleft()
            b_card = self.b_player.popleft()
            a_on_top = (randint(0, 1) == 0)

            if a_card > b_card:
                if len(self.pile) > 0:
                    self.append_pile(self.a_player)
                if a_on_top:
                    self.append_cards(self.a_player, b_card, a_card)
                else:
                    self.append_cards(self.a_player, a_card, b_card)
            elif b_card > a_card:
                if len(self.pile) > 0:
                    self.append_pile(self.b_player)
                if a_on_top:
                    self.append_cards(self.b_player, b_card, a_card)
                else:
                    self.append_cards(self.b_player, a_card, b_card)
            else:
                if a_on_top:
                    self.append_cards(self.pile, b_card, a_card)
                else:
                    self.append_cards(self.pile, a_card, b_card)
            self.counter += 1
            if debug_print:
                self.summarize_turn(a_card, b_card)
        return self.counter

    def game_over(self):
        return len(self.a_player) == 0 or len(self.b_player) == 0

    def append_cards(self, hand, card_1, card_2):
        hand.append(card_1)
        hand.append(card_2)

    def append_pile(self, hand):
        """
        Adds all the cards in the pile to the hand passed in (preserving order)
        Also clears the pile.
        """
        hand.extend(self.pile)
        self.pile.clear()

    def summarize_turn(self, a_card, b_card):
        if a_card > b_card:
            print('A WINS')
        elif b_card > a_card:
            print('B WINS')
        else:
            print('TIE')

        print('TURN: {}'.format(self.counter))
        print('a-card: {} b-card: {}'.format(a_card, b_card))
        print('a-length: {} b-length: {}'.format(len(self.a_player),
              len(self.b_player)))
        print()
