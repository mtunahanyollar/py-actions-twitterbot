import os
import tweepy

## Auth
def post_date():
    import hltv
    return hltv.get_matches()

# tt = tweepy.Client(
#     #Consumer Keys
#     consumer_key= os.environ['CONSUMER_API_KEY'],
#     consumer_secret= os.environ['CONSUMER_API_SECRET'],
#     # Access Token and Secret
#     access_token= os.environ['ACCESS_TOKEN'],
#     access_token_secret= os.environ['ACCESS_TOKEN_SECRET'])
  
# ## Defining Functions
print("TEST")
#tt.create_tweet(text="/Automated TEST")
print(post_date())
print("TEST2")

