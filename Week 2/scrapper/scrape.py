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
            # consumer_key = '1fXGFzEGr36eEUYHAf8gTS2kd',
            # consumer_secret = 'kaSi713nLqJnPteuKrs6dS3NjNIbr4MrO3hOctzknpn0dv3Qmd',
            # access_token = '3142951813-k2lvhSNMBFcR9MO4OIJM1iJzdSOSNGr0mDtvtfv',
            # access_token_secret = 'a1hIssTsvTMIi96wnlPTmQg1cV8YlEN3yLRwDhjb3qEhx',
            
            # consumer_key='JAGHqHqesqDk3No6qF5yIy0G0',
            # consumer_secret='DlI1kAV736v3vtynBkZyGgLPQHym1Za2GU6ntZREshlnaRt7Kf',
            # access_token='3142951813-wtP1jki64DKbwXuUaRyRLrHWGFbETOEs7vcahsK',
            # access_token_secret='S3n3JpUUTyQzKZ6WmxLWO3PrKBX6QbSKfg7i0jT64XiIb'
            
            # consumer_key='rKb4owuECdMMX8xdUXyBk6r8n',
            # consumer_secret='OcCA0MAasc2ZjhljPmsN4cwnNe1AxwdNt3CyF5W6tf3an42pwh',
            # access_token='982785281207156738-CKu51wyk5V6u7H03X0Akk2vB0sGiH2i',
            # access_token_secret='KwoRtfI5rwyMHNxUy1wFC3YEifLU468OJ36SYY8JbN24y'
            
            # consumer_key='SWkBwUqZdke8xGjBJaAltkNF4',
            # consumer_secret='sDArrtLFv7N4MJNg2auGAQTlbj4KpskQIS4yDgYfCoSwbOMQO2',
            # access_token='982789481576054786-bRNKtpvGwWNWSI6eNiJXLWg0PfQMNhu',
            # access_token_secret='EHToKpoEoMIoNDBOiWL4lQJc0LMlRWXk3sjVWHridbPCE'
            
            # consumer_key='ThWzAR6yCxdzENE8u2agTii53',
            # consumer_secret='IPZ5ZkzQ1xmHCvJTcYpt0FRCCi2nd7psiqQULIgjCPAQkg3bqY',
            # access_token='982785281207156738-De2NxwLPZh3OrB26r8o7T7Hb9TIBjjg',
            # access_token_secret='wFIO9T8Lnbc6xtUwc5YcVxsBB4NB49Ga6sG0M4SUovtYx'
            
            # consumer_key='dTfJcReLzKGr2CPg6DP3synVc',
            # consumer_secret='vVvTVZzcrGVMf7IL91s1fw1B3cDgmIEtSvDWhbyu9tVasGQNSP',
            # access_token='982789481576054786-TLBXX6h8Lvm2vvCmkFqV6gluMsN5PH7',
            # access_token_secret='K8cpyfPjApwNXQfbksCLV6N5fnMSXsI74yvHMyRMGnNMd'
            
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

df.to_pickle("C:\Users\AK\Dropbox\Data Science\Personal\52WeeksOfMachineLearning\Week 2\data\nbatweets")


# Short Cuts
df    
df.loc[0,"Test"] = "Frank"
df.columns
df.drop(['tweets', 'Test'], inplace=True,axis=1)
df["tweets"][0]
