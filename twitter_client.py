import os
import tweepy

class TwitterClient:
    def __init__(self):
        # Retrieve Twitter API credentials from environment variables
        # Authenticate with Twitter API
        newClient = tweepy.Client(
            consumer_key= os.environ['CONSUMER_API_KEY'],
            consumer_secret= os.environ['CONSUMER_API_SECRET'],
            access_token= os.environ['ACCESS_TOKEN'],
            access_token_secret= os.environ['ACCESS_TOKEN_SECRET']
        )

        # Create the Tweepy Client
        self.client = newClient

    def get_client(self):
        # Return the Tweepy Client
        return self.client

