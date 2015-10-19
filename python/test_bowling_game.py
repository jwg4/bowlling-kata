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

    def test_one_spare(self):
        self.g.roll(5)
        self.g.roll(5)
        self.g.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(self.g.score(), 16)

    def test_successive_rolls_sum_to_10(self):
        """ Two rolls sum to ten, but which are part of different frames."""
        self.g.roll(3)
        self.g.roll(5)
        self.g.roll(5)
        self.roll_many(17, 0)
        self.assertEqual(self.g.score(), 13)

    def test_one_strike(self):
        self.g.roll(10)
        self.g.roll(5)
        self.g.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(self.g.score(), 26)

    def test_300_game(self):
        self.roll_many(12, 10)
        self.assertEqual(self.g.score(), 300)

