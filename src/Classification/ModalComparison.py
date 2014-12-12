__author__ = 'stanley'

from numpy import *
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.lda import LDA
from sklearn import linear_model
from sklearn.metrics import roc_curve, auc


nbaData = genfromtxt('../../NBA2012-15/Classification/NBA12_14.csv', delimiter=',')
nba15test = genfromtxt('../../NBA2012-15/Classification/NBA15.csv', delimiter=',')


# May perform better with standardize features
# For easy implementation, I convert data to the base 10 logarithm
nba15test_scaled = nba15test
nba15test_scaled[:,1:] = log10(nba15test_scaled[:,1:])

label = nbaData[:,0]
features = log10(nbaData[:,1:])


svm = svm.SVC(kernel='rbf', probability=True, C=1)
lda = LDA(n_components=2)
logistic =linear_model.LogisticRegression(penalty='l1',C=10)


classifiers= [svm,lda,logistic]
name = ['Linear SVM C=1','LDA','Logistic L1 C=10']
color =['red','blue','black']

for classifier ,n, c in zip(classifiers,name,color):
    prob15 = classifier.fit(features, label).predict_proba(nba15test_scaled[:,1:])
    fpr15, tpr15, thresholds15 = roc_curve(nba15test_scaled[:,0], prob15[:, 1])
    roc_auc15 = auc(fpr15, tpr15)
    plt.plot(fpr15, tpr15,
                     label='%s (area = %0.2f)' % (n, roc_auc15), lw=3, color=c)


plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Model Comparison using NBA 2015 games')
plt.legend(loc="lower right")
plt.show()

