class BowlingGame(object):
    def __init__(self):
        self._score = 0
        self._previous = 0
        self.count_double = False

    def score(self):
        return self._score

    def roll(self, pins):
        self._score = self._score + pins
        if self.count_double:
            self._score = self._score + pins
        if pins + self._previous == 10:
            self.count_double = True
        else:
            self.count_double = False
        self._previous = pins

