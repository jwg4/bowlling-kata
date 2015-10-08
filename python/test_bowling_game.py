import unittest

from game import Game

class BowlingGameTest(unittest.TestCase):
    def test_gutter_game(self):
        g = Game()
        for i in range(20):
            g.roll(0)

