# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:14:59 2016

@author: siham.belgadi
"""

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
import lda
import numpy as np
from numpy import *


tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# create sample documents
doc_a = "Management Capabilities: Canadian entrepreneurs identify the need for more capability."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health." 


# créer un dictionnaire

dic ={}

# compile sample documents into a list
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# list for tokenized documents in loop
texts = []

listMot = []
j = 0
# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    
    for i in stopped_tokens:
        listMot.append(p_stemmer.stem(i))
        dic[j]=p_stemmer.stem(i)
        j=j+1
    # add tokens to list
    texts.append(stemmed_tokens)
   
    


fichier=open("token.txt",'w')

for cle,valeur in dic.items():
    bla = str(cle) +" "+str(valeur) 
    print(bla)
    fichier.write(bla+"\n")
  
fichier.close() 





#data = numpy.genfromtxt('matrix.csv', delimiter=',')
#print(data)




#print(texts)
#print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#p= numpy.array(texts)
#print(p)
#print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    # turn our tokenized documents into a id <-> term dictionary
#dictionary = corpora.Dictionary(texts)
#dictionary.save('questions.dict');
#corpus = [dictionary.doc2bow(text) for text in texts]
#corpora.MmCorpus.serialize('questions.mm', corpus)
#corpora.SvmLightCorpus.serialize('questions.svmlight', corpus)
#corpora.BleiCorpus.serialize('questions.lda-c', corpus)
#corpora.LowCorpus.serialize('questions.low', corpus)


#corpora.BleiCorpus.serialize('questions.lda-c', corpus)
#mm = corpora.MmCorpus('questions.mm')



# corpus, is a list of vectors equal to the number of documents
#The tuples are (term ID, term frequency)

#print(corpus)


#print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

#pp= numpy.array(corpus)
#print(pp)

#pp = numpy.squeeze(numpy.asarray(corpus))



#matr = lda.utils.matrix_to_lists(pp)

#print(matr)



#for doc in corpus:
    #print(doc)






































