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
        game = Egrt(0.26)
        self.assertTrue(game.a_won_slap())

    @patch('games.egrt.random')
    def test_random_same_as_a_slap_probability(self, random_mock):
        random_mock.return_value = 0.26
        game = Egrt(0.26)
        self.assertFalse(game.a_won_slap())

    @patch('games.egrt.random')
    def test_random_greater_than_a_slap_probability(self, random_mock):
        random_mock.return_value = 0.27
        game = Egrt(0.26)
        self.assertFalse(game.a_won_slap())

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

    def test_is_slap_empty_pile(self):
        game = Egrt(0.5)
        self.assertFalse(game.is_slap(Card(Rank.FIVE, Suit.CLUB)))

    def test_is_slap_single_card_in_pile(self):
        game = Egrt(0.5)
        game.top_card = Card(Rank.JACK, Suit.DIAMOND)
        self.assertTrue(game.is_slap(Card(Rank.JACK, Suit.HEART)))

    def test_is_slap_not_a_slap(self):
        game = Egrt(0.5)
        game.prev_card = Card(Rank.SEVEN, Suit.CLUB)
        game.top_card = Card(Rank.SIX, Suit.DIAMOND)
        self.assertFalse(game.is_slap(Card(Rank.FIVE, Suit.HEART)))

    def test_is_slap_yes_is_slap(self):
        game = Egrt(0.5)
        game.prev_card = Card(Rank.ACE, Suit.CLUB)
        game.top_card = Card(Rank.QUEEN, Suit.DIAMOND)
        self.assertTrue(game.is_slap(Card(Rank.ACE, Suit.HEART)))

    def test_is_slap_sandwich_slap(self):
        game = Egrt(0.5)
        game.prev_card = Card(Rank.SEVEN, Suit.CLUB)
        game.top_card = Card(Rank.SIX, Suit.DIAMOND)
        self.assertTrue(game.is_slap(Card(Rank.SIX, Suit.HEART)))

    def test_is_slap_queen_king_slap(self):
        game = Egrt(0.5)
        game.prev_card = Card(Rank.SIX, Suit.DIAMOND)
        game.top_card = Card(Rank.QUEEN, Suit.DIAMOND)
        self.assertTrue(game.is_slap(Card(Rank.KING, Suit.SPADE)))

    def test_is_slap_king_queen_slap(self):
        game = Egrt(0.5)
        game.prev_card = Card(Rank.SIX, Suit.DIAMOND)
        game.top_card = Card(Rank.KING, Suit.DIAMOND)
        self.assertTrue(game.is_slap(Card(Rank.QUEEN, Suit.SPADE)))


    def test_is_slap_queen_king_sandwich(self):
        game = Egrt(0.5)
        game.prev_card = Card(Rank.KING, Suit.DIAMOND)
        game.top_card = Card(Rank.SIX, Suit.DIAMOND)
        self.assertFalse(game.is_slap(Card(Rank.QUEEN, Suit.SPADE)))

    def test_is_slap_king_queen_sandwich(self):
        game = Egrt(0.5)
        game.prev_card = Card(Rank.QUEEN, Suit.DIAMOND)
        game.top_card = Card(Rank.SIX, Suit.DIAMOND)
        self.assertFalse(game.is_slap(Card(Rank.KING, Suit.SPADE)))
