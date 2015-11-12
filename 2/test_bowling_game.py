import unittest
import hypothesis
import hypothesis.strategies

from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def test_score_before_any_rolls(self):
        game = BowlingGame()
        self.assertEqual(game.score(), 0)

    @hypothesis.given(hypothesis.strategies.integers(0, 10))
    def test_single_roll(self, x):
        game = BowlingGame()
        game.roll(x)
        self.assertEqual(game.score(), x)

