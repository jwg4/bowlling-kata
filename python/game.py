class Game(object):
    scores = []

    def roll(self, pins):
        self.scores.append(pins)

    def score(self):
        return sum(self.scores)
