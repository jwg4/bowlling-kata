import unittest

from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def test_game(self):
        game = BowlingGame()
        self.assertEqual(game.score(), 0)

