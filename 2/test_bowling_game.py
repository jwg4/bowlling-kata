import unittest
import hypothesis
import hypothesis.strategies

from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def test_score_before_any_rolls(self):
        self.assertEqual(self.game.score(), 0)

    @hypothesis.given(hypothesis.strategies.integers(0, 10))
    def test_single_roll(self, x):
        self.game = BowlingGame()
        self.assertEqual(self.game.score(), 0)
        self.game.roll(x)
        self.assertEqual(self.game.score(), x)

    def test_two_rolls(self):
        self.game.roll(3)
        self.game.roll(2)
        self.assertEqual(self.game.score(), 5)

    def test_spare(self):
        self.game.roll(4)
        self.game.roll(6)
        self.game.roll(5)
        self.assertEqual(self.game.score(), 20)

