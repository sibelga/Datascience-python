# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 11:55:27 2016

@author: siham.belgadi
"""

import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'C:/twitter/scripts/collect/data/data/2016-06-07_tweets.json'

tweets_data = []
text_data=[]
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
    

print len(tweets_data)

i = 0

text = ""

while(i<len(tweets_data)):
    text = text + " "+tweets_data[i]['text']+" "+"\n"
    i=i+1


#print(text)
#tweets = pd.DataFrame()

cash = []
 
text_data.append("a")     

for t in tweets_data:
        if t['text'] in text_data:
            print("ok \n")
        if t['text'] not in text_data:
            print("NO \n")
            text_data.append(t['text'])
            
#for x in text_data:
 #   print(x)

     
     
i = 0
while  i< len(text_data):
    if ('$') in text_data[i]:
        cash.append(text_data[i])
        print("yep")
        i=i+1
    else:
        print("nope")
        i=i+1

for x in cash:
    print(x)
        
     
     
     
     
     


#tweets['Jean-Paul Agon'] = map(lambda tweet: tweet['text'], tweets_data)

#☺print(tweets['Jean-Paul Agon'])

#tweets_by_country = tweets['Jean-Paul Agon'].value_counts()

#fig, ax = plt.subplots()
#ax.tick_params(axis='x', labelsize=15)
#ax.tick_params(axis='y', labelsize=10)
#ax.set_xlabel('Countries', fontsize=15)
#ax.set_ylabel('Number of tweets' , fontsize=15)
#ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
#tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')