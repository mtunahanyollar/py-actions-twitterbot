import os
import tweepy


# def post_date():
#     import hltv
#     return hltv.top30teams()

## Auth
# tt = tweepy.Client(
#     #Consumer Keys
#     consumer_key= os.environ['CONSUMER_API_KEY'],
#     consumer_secret= os.environ['CONSUMER_API_SECRET'],
#     # Access Token and Secret
#     access_token= os.environ['ACCESS_TOKEN'],
#     access_token_secret= os.environ['ACCESS_TOKEN_SECRET'])
  
# ## Defining Functions

import hltv
    
print("TEST")
#tt.create_tweet(text="/Automated TEST")
print(hltv.top30teams())
print(hltv.top_players())
print(hltv.get_team_info('6665'))
print("TEST2")

