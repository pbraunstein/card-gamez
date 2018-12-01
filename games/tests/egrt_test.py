import unittest
from unittest.mock import patch

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

    @patch('games.egrt.random')
    def test_random_less_than_a_slap_probability(self, random_mock):
        random_mock.return_value = 0.25
        a = Egrt(0.26)
        self.assertTrue(a.a_won_slap())

    @patch('games.egrt.random')
    def test_random_same_as_a_slap_probability(self, random_mock):
        random_mock.return_value = 0.26
        a = Egrt(0.26)
        self.assertFalse(a.a_won_slap())

    @patch('games.egrt.random')
    def test_random_greater_than_a_slap_probability(self, random_mock):
        random_mock.return_value = 0.27
        a = Egrt(0.26)
        self.assertFalse(a.a_won_slap())

    def test_set_chances_remaining_non_face_card(self):
        game = Egrt(0.5)
        game.top_card = Card(Rank.TEN, Suit.HEART)
        with self.assertRaises(ValueError):
            game.set_chances_remaining()

    def test_set_chances_remaining_ace(self):
        game = Egrt(0.5)
        game.top_card = Card(Rank.ACE, Suit.HEART)
        game.set_chances_remaining()
        self.assertEqual(game.chances_remaining, 4)

    def test_set_chances_remaining_ace(self):
        game = Egrt(0.5)
        game.top_card = Card(Rank.KING, Suit.CLUB)
        game.set_chances_remaining()
        self.assertEqual(game.chances_remaining, 3)
        
    def test_set_chances_remaining_ace(self):
        game = Egrt(0.5)
        game.top_card = Card(Rank.QUEEN, Suit.DIAMOND)
        game.set_chances_remaining()
        self.assertEqual(game.chances_remaining, 2)

    def test_set_chances_remaining_ace(self):
        game = Egrt(0.5)
        game.top_card = Card(Rank.JACK, Suit.SPADE)
        game.set_chances_remaining()
        self.assertEqual(game.chances_remaining, 1)
