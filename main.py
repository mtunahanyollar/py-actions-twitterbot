import random
from chat_gpt_client import ChatGptClient
from twitter_client import TwitterClient

def main():
    # Initialize ChatGptClient
    chat_gpt_client = ChatGptClient()
    topics = ["Bana bir film onerisinde bulun ve en fazla 30 kelime bu filmi ozetle", "Bir Serdar Ortac sarkisi sec ve bir dortluk yaz sonuna serdar ortac'i da ekle.", "Guzel bir ingilizce kelime ve turkce anlamiyla birlikte paylas. en fazla 30 kelime.", "Turk bir sairden alinti yap; dortlukten ileriye gitmesin"]
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
