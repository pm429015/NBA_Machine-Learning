__author__ = 'stanley'

from sklearn.lda import LDA
from numpy import *
from sklearn.linear_model import Ridge

nbaTrain = genfromtxt('../NBA2012-15/Classification/NBA12_14.csv', delimiter=',')
test = genfromtxt('../NBA2012-15/2015GameAfterDec10.csv', delimiter=';')


label = nbaTrain[:,0]
features = nbaTrain[:,1:]

# Training phase
classifier = LDA(n_components=2)
# Testing Phase
result = classifier.fit(features, label).predict(test)
# Save the result
savetxt("../NBA2012-15/NBA_forecast_WinLose.csv", result,delimiter=",", fmt='%1.1f',)

# train = nbaTrain
# train[:,1:] = log10(nbaTrain[:,1:])
#
# regression = Ridge(alpha=0.05)
#
# regression.fit(train[:,1:],train[:,0])
#
# print regression.predict(test)