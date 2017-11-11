# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:57:23 2016

@author: siham.belgadi
"""

import numpy as np
from sklearn.lda import LDA

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
y = np.array([1, 1, 1, 2, 2, 2])
clf = LDA()
clf.fit(X, y)
LDA(n_components=None, priors=None, shrinkage=None, solver='svd',
  store_covariance=False, tol=0.0001)
print(clf.predict([[-0.8, -1]]))