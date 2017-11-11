# -*- coding: utf-8 -*-
"""
Created on Tue May 24 10:00:18 2016

@author: siham.belgadi
"""

import gensim



model = gensim.models.Word2Vec.load('job_titles_1803.model')
t = model.similarity('head', 'ceo')




print(t)