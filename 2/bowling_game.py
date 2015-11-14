class BowlingGame(object):
    def __init__(self):
        self._score = 0

    def score(self):
        return self._score

    def roll(self, pins):
        self._score = self._score + pins
