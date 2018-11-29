import unittest

from model.card import Card
from model.rank import Rank
from model.suit import Suit

class TestCard(unittest.TestCase):
    def test_eq_operator(self):
        self.assertTrue(Card(Rank.TWO, Suit.SPADE) == Card(Rank.TWO, Suit.DIAMOND))
        self.assertFalse(Card(Rank.ACE, Suit.SPADE) == Card(Rank.KING, Suit.SPADE))

    def test_ne_operator(self):
        self.assertTrue(Card(Rank.ACE, Suit.SPADE) != Card(Rank.KING, Suit.SPADE))
        self.assertFalse(Card(Rank.TWO, Suit.SPADE) != Card(Rank.TWO, Suit.DIAMOND))

    def test_lt_operator(self):
        self.assertTrue(Card(Rank.KING, Suit.DIAMOND) < Card(Rank.ACE, Suit.DIAMOND))
        self.assertFalse(Card(Rank.KING, Suit.SPADE) < Card(Rank.QUEEN, Suit.SPADE))

        # lt is strict
        self.assertFalse(Card(Rank.KING, Suit.SPADE) < Card(Rank.KING, Suit.DIAMOND))

    def test_gt_operator(self):
        self.assertTrue(Card(Rank.KING, Suit.SPADE) > Card(Rank.QUEEN, Suit.SPADE))
        self.assertFalse(Card(Rank.KING, Suit.DIAMOND) > Card(Rank.ACE, Suit.DIAMOND))

        # gt is strict
        self.assertFalse(Card(Rank.KING, Suit.SPADE) > Card(Rank.KING, Suit.DIAMOND))

    def test_le_operator(self):
        self.assertTrue(Card(Rank.TWO, Suit.HEART) <= Card(Rank.SIX, Suit.CLUB))
        self.assertFalse(Card(Rank.THREE, Suit.DIAMOND) <= Card(Rank.TWO, Suit.SPADE))

        # le is not strict
        self.assertTrue(Card(Rank.KING, Suit.SPADE) <= Card(Rank.KING, Suit.DIAMOND))

    def test_ge_operator(self):
        self.assertTrue(Card(Rank.THREE, Suit.DIAMOND) >= Card(Rank.TWO, Suit.SPADE))
        self.assertFalse(Card(Rank.TWO, Suit.HEART) >= Card(Rank.SIX, Suit.CLUB))

        # ge is not strict
        self.assertTrue(Card(Rank.KING, Suit.SPADE) >= Card(Rank.KING, Suit.DIAMOND))

    def test_wrong_rank_class_raises_erorr(self):
        with self.assertRaises(TypeError):
            _ = Card(2, Suit.SPADE)

    def test_wrong_suit_class_raises_error(self):
        with self.assertRaises(TypeError):
            _ = Card(Rank.ACE, 1)
