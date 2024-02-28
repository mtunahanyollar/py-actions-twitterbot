import random
from chat_gpt_client import ChatGptClient
from twitter_client import TwitterClient

def main():
    # Initialize ChatGptClient
    chat_gpt_client = ChatGptClient()
    topics = ["Twitter fenomeni oldugunu dusun ve gunde birkac kez hayvanlar alemi hakkinda degisik bilgiler paylastigini dusun, 280 karakteri gecmeyen bilgiler paylas.", "Twitter fenomeni olduğunu düşün ve gunde birkac kez dunyadan degisik bilgiler paylasiyorsun simdi bana 280 karakter sinirini asmayan bir bilgi paylas. YARATICI OL!"]
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
