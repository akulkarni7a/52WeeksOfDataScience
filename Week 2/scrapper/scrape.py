from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from TwitterSearch import *
import string

df = pd.read_csv(r"C:\Users\AK\Dropbox\Data Science\Personal\52WeeksOfMachineLearning\Week 2\data\nba_2017_players_with_salary_wiki_twitter.csv")
df.head()

def searchTwitter(name, index):
    tweetArray = []

    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([name]) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see German tweets only
        tso.set_include_entities(False) # and don't give us all those entity information
    
        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            # consumer_key = '',
            # consumer_secret = '',
            # access_token = '',
            # access_token_secret = '',

         )
    
         # this is where the fun actually starts :)
        for tweet in ts.search_tweets_iterable(tso):
            if "RT" not in tweet['text']:
                tweetArray.append(str(tweet['text']))
      
            else:
                print("")
       
        tweetString = ''.join(tweetArray)
        # print(tweetString.translate(string.punctuation))
        df.loc[index,"tweets"] = tweetString
        
    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)

len(df.index)
df["PLAYER"][0]

for item in range(0,len(df.index)):
    searchTwitter(df["PLAYER"][item],item)



# Short Cuts
df    
df.loc[0,"Test"] = "Frank"
df.columns
df.drop(['tweets', 'Test'], inplace=True,axis=1)
df["tweets"][0]
