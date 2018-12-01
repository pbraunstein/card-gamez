from collections import deque
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

    def test_add_card_to_hand_no_top_or_prev(self):
        game = Egrt(0.5)
        with self.assertRaises(ValueError):
            game.add_cards_to_hand(deque())

    def test_add_cards_to_hand_no_top_card(self):
        game = Egrt(0.5)
        game.prev_card = Card(Rank.THREE, Suit.CLUB)
        with self.assertRaises(ValueError):
            game.add_cards_to_hand(deque())

    def test_add_cards_to_hand_no_prev_card(self):
        game = Egrt(0.5)
        game.top_card = Card(Rank.THREE, Suit.CLUB)
        with self.assertRaises(ValueError):
            game.add_cards_to_hand(deque())

    def test_add_cards_to_hand_no_pile(self):
        game = Egrt(0.5)
        card_1 = Card(Rank.FOUR, Suit.HEART)
        card_2 = Card(Rank.JACK, Suit.CLUB)

        game.prev_card = card_1
        game.top_card = card_2

        actual_hand = deque()
        game.add_cards_to_hand(actual_hand)
        self.assertEqual(list(actual_hand), [card_1, card_2])

    def test_add_cards_to_hand_single_card_in_pile(self):
        game = Egrt(0.5)
        card_1 = Card(Rank.FOUR, Suit.HEART)
        card_2 = Card(Rank.SIX, Suit.SPADE)
        card_3 = Card(Rank.QUEEN, Suit.CLUB)

        game.pile.append(card_1)
        game.prev_card = card_2
        game.top_card = card_3

        actual_hand = deque()
        game.add_cards_to_hand(actual_hand)
        self.assertEqual(list(actual_hand), [card_1, card_2, card_3])
        
    def test_add_cards_to_hand_multiple_cards_in_pile(self):
        game = Egrt(0.5)
        card_1 = Card(Rank.FOUR, Suit.HEART)
        card_2 = Card(Rank.SIX, Suit.SPADE)
        card_3 = Card(Rank.QUEEN, Suit.CLUB)
        card_4 = Card(Rank.TEN, Suit.DIAMOND)
        card_5 = Card(Rank.EIGHT, Suit.CLUB)
        card_6 = Card(Rank.TWO, Suit.CLUB)
        card_7 = Card(Rank.NINE, Suit.SPADE)

        game.pile.extend([card_1, card_2, card_3, card_4, card_5])
        game.prev_card = card_6
        game.top_card = card_7

        actual_hand = deque()
        game.add_cards_to_hand(actual_hand)
        self.assertEqual(list(actual_hand),
                [card_1, card_2, card_3, card_4, card_5, card_6, card_7])

