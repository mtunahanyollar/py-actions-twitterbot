from chat_gpt_client import ChatGptClient
from twitter_client import TwitterClient

def main():
    # Initialize ChatGptClient
    chat_gpt_client = ChatGptClient()

    # Generate response using ChatGptClient
    user_message = "Bana bir film onerisinde bulun ve en fazla 30 kelime bu filmi ozetle"
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
