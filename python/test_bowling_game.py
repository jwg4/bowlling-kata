import unittest

from game import Game

class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.g = Game()

    def roll_many(self, n, pins):
        for i in range(n):
            self.g.roll(pins)

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(self.g.score(), 0)

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.g.score(), 20)

