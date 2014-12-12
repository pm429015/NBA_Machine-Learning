from src.DataHandler.GameResultWithTeamStats import GameResultWithTeamsStats
from src.DataHandler.TestingSamples import TestingSamples

__author__ = 'stanley'

from numpy import genfromtxt
from numpy import savetxt


class DataCombiner:

    def __init__(self, data1, data2):
        self.data1 =data1
        self.data2 = data2

    # invoke a rule object that implements concert rule
    def combine(self,rule):
        rule.schedule = self.data1
        rule.teamStats = self.data2
        self.result = rule.rule()


    def saveResult(self):
        if self.result is not None:
            savetxt("../../NBA2012-15/NBATesting.csv", self.result,delimiter=",", fmt='%1.3f',)
        else:
            print "No result data yet!"





schedule = genfromtxt('../../NBA2012-15/leagues_NBA_2015_games_games.csv', delimiter=';', dtype="S", skip_header=1)
teamStats = genfromtxt('../../NBA2012-15/leagues_NBA_2015_misc.csv', delimiter=';', dtype="S", skip_header=1)

combiner = DataCombiner(schedule,teamStats)


combiner.combine(TestingSamples())
combiner.saveResult()

