class Game(object):
    def __init__(self):
        self.scores = []

    def roll(self, pins):
        self.scores.append(pins)

    def score(self):
        total = 0
        for i in range(len(self.scores)):
            s = self.scores[i]
            total = total + s
            if s + self.scores[i+1] == 10:
                total = total + self.scores[i+1]
        return total
