class Game(object):
    score_ = 0

    def roll(self, pins):
        self.score_ = self.score_ + pins

    def score(self):
        return self.score_
