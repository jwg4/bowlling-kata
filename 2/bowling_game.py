class BowlingGame(object):
    def __init__(self):
        self._score = 0
        self._previous = 0
        self._count_double = False
        self._end_of_frame = False

    def score(self):
        return self._score

    def roll(self, pins):
        self._score = self._score + pins
        if self._count_double:
            self._score = self._score + pins
        self._count_double = False
        if self._end_of_frame:
            self._end_of_frame = False
            if pins + self._previous == 10:
                self._count_double = True
        elif pins == 10:
            self._count_double = True
            self._end_of_frame = False
        else:
            self._end_of_frame = True
        self._previous = pins

