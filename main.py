import random
from chat_gpt_client import ChatGptClient
from twitter_client import TwitterClient

def main():
    # Initialize ChatGptClient
    chat_gpt_client = ChatGptClient()
    topics = ["Emek ve dayanışma üzerine şiirler yazdığını düşün türk şairlerden şiir seç ve paylaş.(Alinti yap)", "Twitter fenomeni olduğunu düşün her gün farklı motivasyon ve emeğe dair tweetler atıyorsun. YARATICI OL!"]
    result = random.choice(topics)
    print(result)
    # Generate response using ChatGptClient
    user_message = "280 KARAKTERİ GEÇME!" + result 
    response = chat_gpt_client.generate_response(user_message)
    print("ChatGPT Response:", response)
    
    # Initialize TwitterClient
    twitter_client = TwitterClient()

    # Get the Twitter Client
    twitter_api_client = twitter_client.get_client()
    print("Twitter Client:", twitter_api_client)
    asTweet = response[:280]
    twitter_api_client.create_tweet(text = asTweet)

if __name__ == "__main__":
    main()
