import unittest

from model.suit import Suit

class TestSuit(unittest.TestCase):
    def test_eq_operator(self):
        self.assertTrue(Suit.DIAMOND == Suit.DIAMOND)
        self.assertFalse(Suit.SPADE == Suit.HEART)

    def test_ne_operator(self):
        self.assertTrue(Suit.CLUB != Suit.SPADE)
        self.assertFalse(Suit.HEART != Suit.HEART)

    def test_eq_with_int_raises_error(self):
        with self.assertRaises(TypeError):
            Suit.SPADE == 1

    def test_ne_with_int_raises_error(self):
        with self.assertRaises(TypeError):
            Suit.DIAMOND != 1

if __name__ == '__main__':
    unittest.main()
