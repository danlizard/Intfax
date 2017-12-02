import twitter
import time
import datetime
from info import *
from TwitterSearch import *

class TSearch:
    def __init__(self, words):
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords(words) # let's define all words we would like to have a look for
        tso.set_language('ru') # we want to see German tweets only
        tso.set_include_entities(False) # and don't give us all those entity information
        ts = TwitterSearch(
            consumer_key = c_key,
            consumer_secret = c_secret,
            access_token = a_key,
            access_token_secret = a_secret
         )
        # this is where the fun actually starts :)
        #print("#")
        self.data = []
        unique = dict()
        def my_callback_closure(current_ts_instance): # accepts ONE argument: an instance of TwitterSearch
                queries, tweets_seen = current_ts_instance.get_statistics()
                if queries > 0 and (queries % 5) == 0: # trigger delay every 5th query
                    time.sleep(60) # sleep for 60 seconds
        
        for tweet in ts.search_tweets_iterable(tso, callback=my_callback_closure):        
            tweet["user"] = None
            if tweet["text"] in unique:
                unique[tweet["text"]][0] = min(unique[tweet["text"]][0], tweet["created_at"])
                unique[tweet["text"]][1] += 1
                unique[tweet["text"]][2] += tweet['retweet_count']
                unique[tweet["text"]][3] += tweet["favorite_count"]
            else:
                unique[tweet["text"]] = [tweet["created_at"], 1, tweet['retweet_count'], tweet["favorite_count"]] #First Date, Posts, Reposts, Likes
                #tweet['retweeted_status'] = len(tweet['retweeted_status'])
                #self.data.append(tweet)
                #print( 'tweeted: %s' % (tweet['text'] ) 
        self.data = unique
    def size(self):
        return len(self.data)
    def get(self):
        return self.data
if __name__== "__main__":
    q = ["Владимир", "Путин", "военные", "рельсы", "производству военной продукции"]
    z =  TSearch(["интерфакс", "путин"]).get()
    print(len(z))
    for el in z:
        print(z[el], el)