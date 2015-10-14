import unittest

from game import Game

class BowlingGameTest(unittest.TestCase):
    def test_gutter_game(self):
        g = Game()
        for i in range(20):
            g.roll(0)
        self.assertEqual(g.score(), 0)

    def test_all_ones(self):
        g = Game()
        for i in range(20):
            g.roll(1)
        self.assertEqual(g.score(), 20)

