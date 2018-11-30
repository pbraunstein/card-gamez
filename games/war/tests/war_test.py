import unittest
from unittest.mock import MagicMock

from games.war.war import War
from model.card import Card
from model.deck import Deck
from model.rank import Rank
from model.suit import Suit

class TestWar(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.mock_deck = Deck()

    def test_wrong_deck_class_raises_error(self):
        with self.assertRaises(TypeError):
            _ = War(42)

    def test_empty_deck_no_turns(self):
        """
        Game is over before it begins. No turns should be recorded.
        """
        self.mock_deck.deal = MagicMock(return_value=([], []))
        game = War(deck=self.mock_deck)
        self.assertEqual(game.simulate_game(), 0) 

    def test_identical_hands_turns_len_of_hand(self):
        """
        The game ends with all cards in the pile. Ultimately a tie.
        """
        self.mock_deck.deal = MagicMock(return_value=(
            [Card(Rank.ACE, Suit.SPADE), Card(Rank.KING, Suit.DIAMOND), Card(Rank.QUEEN, Suit.SPADE)],
            [Card(Rank.ACE, Suit.HEART), Card(Rank.KING, Suit.CLUB), Card(Rank.QUEEN, Suit.DIAMOND)]
        ))
        game = War(deck=self.mock_deck)
        self.assertEqual(game.simulate_game(), 3)

    def test_hands_of_different_sizes(self):
        """
        The game can end when only one player is out of cards
        """
        self.mock_deck.deal = MagicMock(return_value=(
            [Card(Rank.ACE, Suit.SPADE), Card(Rank.KING, Suit.DIAMOND), Card(Rank.QUEEN, Suit.SPADE)],
            [Card(Rank.KING, Suit.HEART), Card(Rank.JACK, Suit.CLUB)] 
        ))
        game = War(deck=self.mock_deck)
        self.assertEqual(game.simulate_game(), 2)

