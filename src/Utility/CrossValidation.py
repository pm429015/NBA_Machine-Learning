__author__ = 'stanley'

from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from numpy import *

class CorssValidation:

    def cv(self,features, label, classifier, testset, title):
        # Classification and ROC analysis
        # Cross validation
        cv = StratifiedKFold(label,5)

        mean_tpr = 0.0
        mean_fpr = linspace(0, 1, 100)
        for i, (train, test) in enumerate(cv):
            probas_ = classifier.fit(features[train], label[train]).predict_proba(features[test])

            # Compute ROC curve and area the curve
            fpr, tpr, thresholds = roc_curve(label[test], probas_[:, 1])
            mean_tpr += interp(mean_fpr, fpr, tpr)
            mean_tpr[0] = 0.0
            roc_auc = auc(fpr, tpr)
            plt.plot(fpr, tpr, lw=1, label='ROC evaluation fold %d (area = %0.2f)' % (i, roc_auc))

        plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')

        mean_tpr /= len(cv)
        mean_tpr[-1] = 1.0
        mean_auc = auc(mean_fpr, mean_tpr)
        plt.plot(mean_fpr, mean_tpr, 'k--',
                 label='Mean ROC (area = %0.2f)' % mean_auc, lw=4, color='black')

        # use all data to train the model and use 2015 data to test
        prob15 = classifier.fit(features, label).predict_proba(testset[:,1:])
        fpr15, tpr15, thresholds15 = roc_curve(testset[:,0], prob15[:, 1])
        roc_auc15 = auc(fpr15, tpr15)
        plt.plot(fpr15, tpr15, 'm--',
                 label='ROC 2015 Test (area = %0.2f)' % roc_auc15, lw=4, color='red')

        plt.xlim([-0.05, 1.05])
        plt.ylim([-0.05, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(title)
        plt.legend(loc="lower right")
        plt.show()