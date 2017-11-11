# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:50:21 2016

@author: siham.belgadi
"""

import tweepy
import time
import json

consumer_key = "Nka73bqa1Y7aynZlxy6U8hfPa"
consumer_secret = "jwh65hSVbx0zeLh5ke11syKXIxHY9W7HEq2mq80RD4MQxwmU3J"
access_token = "742640464873066496-ruHKNh30qx0j35l3h9hRQ7yRdgJbh4y"
access_token_secret = "nfp6IoV3bcSst9bkTP9LdGjrPRMJA9j6F2laKlcqc0Ko3"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

a=[]
output_dir = "."

page_count = 0

for tweet in tweepy.Cursor(api.search,
                           q="CEO Ben van Beurden",
                           count=25,
                           result_type="recent",
                           include_entities=True,
                           lang="fr").items():
    page_count += 1
    #Enregistrement dans la matrice a des tweets
    a.append([tweet.created_at,tweet.text])
    day = tweet.created_at.strftime('%Y-%m-%d')
    
    with open( "%s/%s_tweets.json" % (output_dir, day), 'a') as f:
                     f.write(json.dumps(a._json))
                     f.write('\n')
             
    print("{0} tweets téléchargés".format(len (a)))
    print len(a)
    time.sleep(0.2)
#Pour respecter la fréquence imposée par l'api, je fais une pause de 0.2 secondes entre 
#chaque résultat

    if tweepy.TweepError is "[{u'message': u'Over capacity', u'code': 130}]":
        print "Over capacity" 
        time.sleep(2000)

    if tweepy.TweepError is "[{u'message': u'Internal error', u'code': 131}]":
        print "Internal error"
        time.sleep(2000) 