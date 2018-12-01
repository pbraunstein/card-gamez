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

    def test_a_slap_probability_negative(self):
        with self.assertRaises(ValueError):
            _ = Egrt(-0.1)

    def test_a_slap_probability_is_one(self):
        with self.assertRaises(ValueError):
            _ = Egrt(1.0)

    def test_a_slap_probability_greater_than_one(self):
        with self.assertRaises(ValueError):
            _ = Egrt(1.25)

    def test_wrong_deck_class_raises_error(self):
        with self.assertRaises(TypeError):
            _ = Egrt(0.5, 12)
