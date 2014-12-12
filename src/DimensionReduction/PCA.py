from src.Utility.ScatterWithHistPlot import ScatterWithHistPlot

__author__ = 'stanley'

from sklearn.decomposition import PCA, KernelPCA
from numpy import genfromtxt
from sklearn import preprocessing

nbaData = genfromtxt('../../NBA2012-15/Classification/NBA12_14.csv', delimiter=',')

label = nbaData[:,0]
features = nbaData[:,1:]

pca = PCA()
pca.fit(features)

#Print out variance
print pca.explained_variance_ratio_

# plot first 2 components
pca.n_components=2
f_reduced = pca.fit_transform(features)


showGraph = ScatterWithHistPlot()
showGraph.plot(f_reduced, label)


