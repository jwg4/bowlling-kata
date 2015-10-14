import unittest

from game import Game

class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.g = Game()

    def test_gutter_game(self):
        for i in range(20):
            self.g.roll(0)
        self.assertEqual(self.g.score(), 0)

    def test_all_ones(self):
        for i in range(20):
            self.g.roll(1)
        self.assertEqual(self.g.score(), 20)

