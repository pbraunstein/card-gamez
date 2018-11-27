import unittest

from rank import Rank

class TestRank(unittest.TestCase):
    def test_eq_operator(self):
        self.assertTrue(Rank.TWO == Rank.TWO)
        self.assertFalse(Rank.KING == Rank.FIVE)

    def test_ne_operator(self):
        self.assertTrue(Rank.SEVEN != Rank.EIGHT)
        self.assertFalse(Rank.JACK != Rank.JACK)

    def test_lt_operator(self):
        self.assertTrue(Rank.TEN < Rank.JACK)
        self.assertFalse(Rank.KING < Rank.FOUR)

        # lt is strict
        self.assertFalse(Rank.SEVEN < Rank.SEVEN)

    def test_gt_operator(self):
        self.assertTrue(Rank.NINE > Rank.EIGHT)
        self.assertFalse(Rank.TWO > Rank.THREE)

        # gt is strict
        self.assertFalse(Rank.SIX > Rank.SIX)

    def test_le_operator(self):
        self.assertTrue(Rank.QUEEN <= Rank.KING)
        self.assertFalse(Rank.ACE <= Rank.KING)

        # le is not strict
        self.assertTrue(Rank.JACK <= Rank.JACK)

    def test_ge_operator(self):
        self.assertTrue(Rank.TEN >= Rank.NINE)
        self.assertFalse(Rank.JACK >= Rank.KING)

        # ge is not strict
        self.assertTrue(Rank.SIX >= Rank.SIX)

    def test_eq_operator_with_int_raises_error(self):
        with self.assertRaises(TypeError):
            Rank.TEN == 10

    def test_ne_operator_with_int_raises_error(self):
        with self.assertRaises(TypeError):
            Rank.TWO != 9

if __name__ == '__main__':
    unittest.main()
