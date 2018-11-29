import unittest

from games.war.war import War

class TestWar(unittest.TestCase):
    def test_wrong_deck_class_raises_error(self):
        with self.assertRaises(TypeError):
            _ = War(42)
