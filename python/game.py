class Game(object):
    def __init__(self):
        self.scores = []

    def roll(self, pins):
        self.scores.append(pins)

    def score(self):
        return sum(self.scores)
