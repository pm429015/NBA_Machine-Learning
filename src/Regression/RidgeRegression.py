__author__ = 'stanley'

from numpy import *
from sklearn.linear_model import Ridge
from sklearn.cross_validation import KFold

nbaData = genfromtxt('../../NBA2012-15/Regression/NBA12_14.csv', delimiter=',')
nba15test = genfromtxt('../../NBA2012-15/Regression/NBA15.csv', delimiter=',')

nba15test_scaled = nba15test
# nba15test_scaled[:,1:] = log10(nba15test_scaled[:,1:])

train = nbaData
# train[:,1:] = log10(nbaData[:,1:])

regression = Ridge(alpha=0.05)



kf = KFold(len(train),k=10)
avgResiduSum = 0
avgVar = 0
for tr, e in kf:
    regression.fit(train[tr,1:],train[tr,0])

    avgResiduSum += mean((regression.predict(train[e,1:]) - train[e,0]) ** 2)

    # Explained variance score: 1 is perfect prediction
    avgVar +=regression.score(train[e,1:] , train[e,0])

print '############'
print 'Evaluation Phase'
avgResiduSum = avgResiduSum/len(kf)
print("Average Residual sum of squares: %.2f" % avgResiduSum )
avgVar = avgVar/len(kf)
print('Average Variance score: %.2f' % avgVar)

print '############'
print 'Testing Phase'
regression.fit(train[:,1:],train[:,0])
print("Residual sum of squares: %.2f"
      % mean((regression.predict(nba15test_scaled[:,1:]) - nba15test_scaled[:,0]) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regression.score(nba15test_scaled[:,1:] , nba15test_scaled[:,0]))



