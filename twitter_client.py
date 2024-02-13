import os
import tweepy

class TwitterClient:
    def __init__(self):
        # Retrieve Twitter API credentials from environment variables
        
        # consumer_key= os.environ['CONSUMER_API_KEY'],
        # consumer_secret= os.environ['CONSUMER_API_SECRET'],
        # access_token= os.environ['ACCESS_TOKEN'],
        # access_token_secret= os.environ['ACCESS_TOKEN_SECRET']

        # Authenticate with Twitter API
        newClient = tweepy.Client(
            consumer_key="SEKkkoFGWfGyW8DsgPNTZkI8J",
            consumer_secret="5bRgHJrhwkz15rRtQark67KLSUGftp2dJ6yoNSL6BEIfxAykFG",
            access_token="1752378513959608321-b1LgFqkmK4uk3ULzFTDNcXJNDaHGnb",
            access_token_secret="InsXd4ysVm9wMb9q7pOgvFi61QXpAv9Z4aJhw3DO3VRN8"
        )

        # Create the Tweepy Client
        self.client = newClient

    def get_client(self):
        # Return the Tweepy Client
        return self.client
 

# ## Defining Functions
    
# gasolineValues = gasoline("ISTANBUL")
# euro_values, usd_values = currencies()
# print("Dolares : " + usd_values["BanknoteSelling"] + " EURO : " + euro_values["BanknoteBuying"])
# finalText = "L o L :  \n"+ "Kursunsuz_95(Excellium95)_TL/lt " + gasolineValues[0] + "\n" + "Motorin(Eurodiesel)_TL/lt " + gasolineValues[1]
# finalText = finalText + "\n\n" + "USD ALIS: " + usd_values["BanknoteBuying"] + "\nUSD SATIS: " + usd_values["BanknoteSelling"]+ "\n\nEURO ALIS: " + euro_values["BanknoteBuying"] + "\nEURO SATIS: " +  euro_values["BanknoteSelling"]
# print(finalText)
# tt.create_tweet(text= finalText)

