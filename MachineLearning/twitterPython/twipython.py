from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import tweepy
import json
import time
import os
import sys

class MyListener(StreamListener):
 
    
    def on_data(self, data):
        try:
            with open('dave.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


consumer_key = "Nka73bqa1Y7aynZlxy6U8hfPa"
consumer_secret = "jwh65hSVbx0zeLh5ke11syKXIxHY9W7HEq2mq80RD4MQxwmU3J"
access_token = "742640464873066496-ruHKNh30qx0j35l3h9hRQ7yRdgJbh4y"
access_token_secret = "nfp6IoV3bcSst9bkTP9LdGjrPRMJA9j6F2laKlcqc0Ko3"
output_dir = "."
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)   
tw_block_size = 100    # Nombre de Tweet par requete
twitter_stream = Stream(auth, MyListener())
tweetCount = 0

while tweetCount < 5:
         try:
             new_tweets = api.search(q='CEO Ben van Beurden', count=tw_block_size)
             for tweet in new_tweets:
                 day = tweet.created_at.strftime('%Y-%m-%d')
                 with open( "%s/%s_tweets.json" % (output_dir, day), 'a') as f:
                     f.write(json.dumps(tweet._json))
                     f.write('\n')
             tweetCount += len(new_tweets)
             print("{0} tweets téléchargés".format(tweetCount))
            
         except tweepy.TweepError as e:
             print("Une erreur est intervenue. Pour poursuivre le processus de collecte, relancer la commande suivante :")
             
             print("")
             print("Error : " + str(e))
             break