__author__ = 'stanley'

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter

class ScatterWithHistPlot:

    def plot(self, f_reduced,label):
        GameWin = f_reduced[np.where(label==1)]
        GameLose = f_reduced[np.where(label==0)]


        nullfmt   = NullFormatter()         # no labels

        # definitions for the axes
        left, width = 0.05, 0.7
        bottom, height = 0.05, 0.7
        bottom_h = left_h = left+width+0.02

        rect_scatter = [left, bottom, width, height]
        rect_histx = [left, bottom_h, width, 0.2]
        rect_histy = [left_h, bottom, 0.2, height]

        # start with a rectangular Figure
        plt.figure(1, figsize=(8,8))

        axScatter = plt.axes(rect_scatter)
        axHistx = plt.axes(rect_histx)
        axHisty = plt.axes(rect_histy)

        # no labels
        axHistx.xaxis.set_major_formatter(nullfmt)
        axHisty.yaxis.set_major_formatter(nullfmt)

        # the scatter plot:
        for i in range(len(f_reduced)):
            if label[i]==1:
                axScatter.scatter(f_reduced[i,0],f_reduced[i,1], color='green', marker='x')
            else:
                axScatter.scatter(f_reduced[i,0],f_reduced[i,1], color='red', marker='^')
        print "total ",i," samples"

        # now determine nice limits by hand:
        binwidth = 0.05
        xymax = np.max( [np.max(np.fabs(GameWin)), np.max(np.fabs(GameLose))]  )
        lim = ( int(xymax/binwidth) + 1) * binwidth

        axScatter.set_xlim( (-lim, lim) )
        axScatter.set_ylim( (-lim, lim) )

        bins = np.arange(-lim, lim + binwidth, binwidth)
        axHistx.hist(GameWin[:,0], bins=bins,color='green', alpha=0.5, label='Win')
        axHistx.hist(GameLose[:,0], bins=bins,color='red', alpha=0.5, label='Lose')

        axHisty.hist(GameWin[:,1], bins=bins, orientation='horizontal',color='green', alpha=0.5)
        axHisty.hist(GameLose[:,1], bins=bins, orientation='horizontal',color='red', alpha=0.5)

        axHistx.set_xlim( axScatter.get_xlim() )
        axHisty.set_ylim( axScatter.get_ylim() )
        axHistx.legend()
        plt.show()