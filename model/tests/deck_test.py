import unittest

from model.card import Card
from model.deck import Deck
from model.model_constants import DoubleDealtDeckError
from model.rank import Rank
from model.suit import Suit

class TestDeck(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.deck = Deck()

    def get_all_cards_in_deck(self):
        cards = []
        for rank in Rank:
            for suit in Suit:
                cards.append(Card(rank, suit))
        return cards

    def test_init(self):
        self.assertEqual(sorted(self.deck.cards),
                         sorted(self.get_all_cards_in_deck()))
        self.assertEqual(len(self.deck.cards), 52)
        self.assertFalse(self.deck.dealt)

    def test_deal(self):
        self.assertFalse(self.deck.dealt)
        player_1, player_2 = self.deck.deal()
        self.assertTrue(self.deck.dealt)
        self.assertEqual(len(player_1), 26)
        self.assertEqual(len(player_2), 26)

        # The hands combined should be the contents of a deck
        self.assertEqual(sorted(player_1 + player_2),
                         sorted(self.get_all_cards_in_deck()))

    def test_double_deal_raise_error(self):
        _, _ = self.deck.deal()
        with self.assertRaises(DoubleDealtDeckError):
            _, _ = self.deck.deal()

