import random
from chat_gpt_client import ChatGptClient
from twitter_client import TwitterClient

def main():
    # Initialize ChatGptClient
    chat_gpt_client = ChatGptClient()
    topics = ["Senin her gun farkli sarki sozleri paylasan bir twitter kullancisi oldugunu dusun; bir Dr Fuchs sarkisindan sozleri paylas.(Alinti yap)", "Senin her gun farkli sarki sozleri paylasan bir twitter kullancisi oldugunu dusun; bir Sansar Salvo sarkisindan sozler paylas.(Alinti yap)"]
    result = random.choice(topics)
    print(result)
    # Generate response using ChatGptClient
    user_message = result
    response = chat_gpt_client.generate_response(user_message)
    print("ChatGPT Response:", response)

    # Initialize TwitterClient
    twitter_client = TwitterClient()

    # Get the Twitter Client
    twitter_api_client = twitter_client.get_client()
    print("Twitter Client:", twitter_api_client)

    twitter_api_client.create_tweet(text = response)

if __name__ == "__main__":
    main()
