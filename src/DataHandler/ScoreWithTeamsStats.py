__author__ = 'stanley'

from numpy import *

from src.DataHandler.ICombineRule import ICombineRule



class ScoreWithTeamsStats(ICombineRule):
    # A helper that generates a list of data sample based on the NBA game
    # Each row represent the result of one game
    # The row contains: Visit team win/lost points, visit team stats features, home team features
    # feature include offense and defense factors (Effective Field Goal Percentage, Turnover Percentage, Offensive Rebound Percentage and Free Throws Per Field Goal Attempt)

    def __init__(self):
        self.schedule = None
        self.teamStats = None


    def rule(self):

        # Check if both data exist
        if self.schedule is not None and self.teamStats is not None:

            # data1 should looks like " Miami Heat;  105; Dallas Mavericks; 94
            # calculate how many points did the first team win? 105-94
            # put it under the first feature
            winScore = self.schedule.T[1].astype(int) - self.schedule.T[3].astype(int)


            # Use a dictionary to keep all teams stats
            stats = {}
            i = 0
            for team in self.teamStats[:, 0]:
                # remove * because raw data used it represent playoff teams
                stats[team.replace("*", "")] = self.teamStats[i, 1:]
                i += 1

            i = 0
            features = ( len(self.teamStats.T) - 1 ) * 2 + 1
            result = zeros((len(winScore), features), dtype=float)
            while i < len(self.schedule):
                tmp = concatenate((stats[self.schedule.T[0, i]], stats[self.schedule.T[2, i]] ), axis=1)

                # sample = concatenate( (result[i],tmp), axis=1   )
                tmp = insert(tmp, 0, winScore[i], axis=0)
                result[i] = tmp
                # print sample
                i += 1

            return result

        else:
            print "Empty input data."