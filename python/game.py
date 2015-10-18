class Game(object):
    def __init__(self):
        self.scores = []

    def roll(self, pins):
        self.scores.append(pins)

    def score(self):
        total = 0
        count = len(self.scores)
        j = 0
        frames = []
        while j < count:
            frame = self.scores[j:j+2]
            if frame[0] == 10:
                frame.append(self.scores[j+2])
                j = j + 1
            elif sum(frame) == 10:
                frame.append(self.scores[j+2])
                j = j + 2
            else:
                j = j + 2
            frames.append(frame)
        for f in frames:
            total = total + sum(f)
        return total
