import unittest

from games.war.war import War

# TODO: Make mock deck and have it return certain hands to test overall game

class TestWar(unittest.TestCase):
    def test_wrong_deck_class_raises_error(self):
        with self.assertRaises(TypeError):
            _ = War(42)
