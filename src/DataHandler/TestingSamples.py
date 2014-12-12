__author__ = 'stanley'

from src.DataHandler.ICombineRule import ICombineRule
from src.DataHandler.ScoreWithTeamsStats import ScoreWithTeamsStats
from numpy import *

class TestingSamples(ICombineRule):
    # A helper that generates a list of testing data sample based on the NBA 2015 game after Dec 10
    # The row contains: visit team stats features and home team features

    def __init__(self):
        self.schedule = None
        self.teamStats = None

    def rule(self):
        # Check if both data exist
        if self.schedule is not None and self.teamStats is not None:


            # Use a dictionary to keep all teams stats
            stats = {}
            i = 0
            for team in self.teamStats[:, 0]:
                # remove * because raw data used it represent playoff teams
                stats[team.replace("*", "")] = self.teamStats[i, 1:]
                i += 1

            i = 0
            features = ( len(self.teamStats.T) - 1 ) * 2
            result = zeros((len(self.schedule), features), dtype=float)
            while i < len(self.schedule):
                tmp = concatenate((stats[self.schedule.T[0, i]], stats[self.schedule.T[2, i]] ), axis=1)
                result[i] = tmp
                # print sample
                i += 1

            return result

        else:
            print "Empty input data."