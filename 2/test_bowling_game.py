import unittest

from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def test_score_before_any_rolls(self):
        game = BowlingGame()
        self.assertEqual(game.score(), 0)

