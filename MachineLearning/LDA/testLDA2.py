# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:18:52 2016

@author: siham.belgadi
"""

import numpy as np
import lda
import lda.datasets
X = lda.datasets.load_reuters()
vocab = lda.datasets.load_reuters_vocab()
titles = lda.datasets.load_reuters_titles()
X.shape

X.sum()

model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X)  # model.fit_transform(X) is also available
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 8
#for i, topic_dist in enumerate(topic_word):
    #topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    #print('Topic {}: {}'.format(i, ' '.join(topic_words)))
    
    
doc_topic = model.doc_topic_
for i in range(10):
 print("{} (top topic: {})".format(titles[i], doc_topic[i].argmax()))