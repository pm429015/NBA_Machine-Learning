__author__ = 'stanley'

from src.Utility.CrossValidation import CorssValidation
from numpy import *
from sklearn import svm

nbaData = genfromtxt('../../NBA2012-15/Classification/NBA12_14.csv', delimiter=',')
nba15test = genfromtxt('../../NBA2012-15/Classification/NBA15.csv', delimiter=',')
# SVM may perform better with standardize features
# For easy implementation, I convert data to the base 10 logarithm
nba15test_scaled = nba15test
nba15test_scaled[:,1:] = log10(nba15test_scaled[:,1:])

label = nbaData[:,0]
features = log10(nbaData[:,1:])



classifier = svm.SVC(kernel='rbf', probability=True, C=1)

#CV
validation = CorssValidation()

validation.cv(features,label,classifier,nba15test, 'ROC for RBF SVM C=1')

