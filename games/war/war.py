from collections import deque
from random import randint
from time import sleep

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

        hand_1, hand_2 = self.deck.deal()
        self.a_player = deque(hand_1)
        self.b_player = deque(hand_2)
        self.pile = deque()
        self.counter = 0

    def simulate_game(self):
        while not self.game_over():
            print('TURN: {}'.format(self.counter))
            print('a-length: {} b-length: {}'.format(len(self.a_player),
                  len(self.b_player)))
            a_card = self.a_player.popleft()
            b_card = self.b_player.popleft()
            a_on_top = (randint(0, 1) == 0)
            print('a-card: {} b-card: {}'.format(a_card, b_card))
            if a_card > b_card:
                print("A WINS")
                if len(self.pile) > 0:
                    self.a_player.extend(self.pile)
                    self.pile.clear()
                if a_on_top:
                    self.a_player.append(b_card)
                    self.a_player.append(a_card)
                else:
                    self.a_player.append(a_card)
                    self.a_player.append(b_card)
            elif b_card > a_card:
                print("B WINS")
                if len(self.pile) > 0:
                    self.b_player.extend(self.pile)
                    self.pile.clear()
                if a_on_top:
                    self.b_player.append(b_card)
                    self.b_player.append(a_card)
                else:
                    self.b_player.append(a_card)
                    self.b_player.append(b_card)
            else:
                print("TIE")
                if a_on_top:
                    self.pile.append(b_card)
                    self.pile.append(a_card)
                else:
                    self.pile.append(a_card)
                    self.pile.append(b_card)
            print()
            self.counter += 1
            sleep(0.01)

    def game_over(self):
        return len(self.a_player) == 0 or len(self.b_player) == 0
