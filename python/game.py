class Game(object):
    def __init__(self):
        self.scores = []

    def roll(self, pins):
        self.scores.append(pins)

    def score(self):
        total = 0
        count = len(self.scores)
        for i in range(count):
            s = self.scores[i]
            total = total + s
            if i + 2 < count and s + self.scores[i+1] == 10:
                total = total + self.scores[i+2]
        return total
