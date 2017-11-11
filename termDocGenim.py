# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:37:37 2016

@author: siham.belgadi
"""

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import os




# create sample documents
mon_fichier = open("sentence.txt", "r")
doc1 = mon_fichier.read()
#print(doc1)




tokenizer = RegexpTokenizer(r'\w+')

raw = doc1.lower()
tokens = tokenizer.tokenize(raw)

print(tokens)

# create English stop words list
en_stop = get_stop_words('en')

# remove stop words from tokens
stopped_tokens = [i for i in tokens if not i in en_stop]
print(stopped_tokens)


# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

texts = []

# stem token
text = [p_stemmer.stem(i) for i in stopped_tokens]
#print(texts)
texts.append(text)

# create document-term matrix 
dictionary = corpora.Dictionary(texts)

corpus = [dictionary.doc2bow(t) for t in texts]
#corpora.BleiCorpus.serialize('/tmp/corpus.lda-c', corpus)

#print(corpus)



MmCorpus = gensim.corpora.mmcorpus



#mCorpus =  gensim.corpora.bleicorpus.BleiCorpus('test.ldac',dictionary)

MmCorpus.MmCorpus.serialize('test.ldac',corpus)

mon = open("fichier.txt", "w")


MmCorpus.MmCorpus.save_corpus('test.ldac',corpus)



mm = MmCorpus.MmCorpus('test.ldac')

mon.writelines


print('le print du mm')

print(mm[0])


# generate LDA model
#ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=20)
#lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=100, update_every=1, chunksize=10000, passes=1)
#lda.print_topics(20)















































