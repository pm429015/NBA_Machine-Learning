__author__ = 'stanley'

from src.Utility.CrossValidation import CorssValidation
from src.Utility.ScatterWithHistPlot import ScatterWithHistPlot
from sklearn.lda import LDA
from numpy import *


nbaData = genfromtxt('../../NBA2012-15/Classification/NBA12_14.csv', delimiter=',')
nba15test = genfromtxt('../../NBA2012-15/Classification/NBA15.csv', delimiter=',')

label = nbaData[:,0]
features = nbaData[:,1:]


# show 2D result
classifier = LDA(n_components=2)
f_reduced = classifier.fit(features,label).transform(features)

show = ScatterWithHistPlot()
show.plot(f_reduced, label)

#CV
validation = CorssValidation()

validation.cv(features,label,classifier,nba15test,'ROC for LDA')









