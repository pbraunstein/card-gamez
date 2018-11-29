import unittest

from model.card import Card
from model.deck import Deck
from model.rank import Rank
from model.suit import Suit

class TestDeck(unittest.TestCase):
    def test_deck_init(self):
        expected_cards = []
        for rank in Rank:
            for suit in Suit:
                expected_cards.append(Card(rank, suit))
        deck = Deck()
        self.assertEqual(sorted(deck.cards), sorted(expected_cards))
        self.assertEqual(len(deck.cards), 52)
        self.assertFalse(deck.dealt)
