class Game(object):
    def __init__(self):
        self.scores = []

    def roll(self, pins):
        self.scores.append(pins)

    def score(self):
        j = 0
        frames = []
        while len(frames) < 10:
            if self.scores[j] == 10:
                # A strike: score for three rolls, start next frame after one
                frame = self.scores[j:j+3]
                j = j + 1
            elif self.scores[j] + self.scores[j+1] == 10:
                # A spare: score for three rolls, start next frame after two
                frame = self.scores[j:j+3]
                j = j + 2
            else:
                # Neither: score for two rolls, start next frame after two
                frame = self.scores[j:j+2]
                j = j + 2
            frames.append(frame)
        return sum(sum(frame) for frame in frames)
