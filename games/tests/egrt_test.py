import unittest

from games.egrt import Egrt
from model.card import Card
from model.deck import Deck
from model.rank import Rank
from model.suit import Suit

class TestEgrt(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.mock_deck = Deck()

    def test_wrong_deck_class_raises_error(self):
        with self.assertRaises(TypeError):
            _ = Egrt(12)
