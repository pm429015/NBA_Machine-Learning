from src.DataHandler.ICombineRule import ICombineRule
from src.DataHandler.ScoreWithTeamsStats import ScoreWithTeamsStats

__author__ = 'stanley'


class GameResultWithTeamsStats(ICombineRule):
    # A helper that generates a list of data sample based on the NBA game
    # Each row represent the result of one game
    # The row contains: Visit team win(1)/lost(0) , visit team stats features, home team features

    def __init__(self):
        self.schedule = None
        self.teamStats = None

    def rule(self):
        rule = ScoreWithTeamsStats()
        rule.schedule = self.schedule
        rule.teamStats = self.teamStats
        result = rule.rule()
        for game in result:
            if(game[0]>0):
                game[0] = 1
            else:
                game[0] = 0

        return result


