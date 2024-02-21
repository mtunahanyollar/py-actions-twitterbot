import os
import openai
import sys
sys.stdout.reconfigure(encoding='utf-8')
class ChatGptClient:
    def __init__(self):
        # Retrieve the API key from the environment variable
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set.")
        
        # Initialize the OpenAI API client with the retrieved API key
        openai.api_key = api_key

    def generate_response(self, user_message):
        # Generate a response from the ChatGPT model given a user message
        completion = openai.chat.completions.create(
        #model="gpt-3.5-turbo-0125",
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": user_message,
            },
        ],
        )
        return completion.choices[0].message.content

        # for chunk in stream:
        #     if chunk.choices[0].delta.content is not None:
        #         print(chunk.choices[0].delta.content, end="")
        #         return chunk.choices[0].delta.content  # Return the generated response text


# from openai import OpenAI

# client = OpenAI(
#   api_key="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"
# )

# input_text = "Cok yaratici bir tweetter kullanicisisin. komik ve ayni zamanda motivasyon odakli tweetler hazirliyorsun. Tweetlerini okuyanlar derhal ise koyulmayi dusunuyorlar, bir ornek verir misin?"
# # Make the API call
# client.Com
# stream = client.chat.completions.create(
#     model="gpt-3.5-turbo-0125",
#     messages=[{"role": "user", "content": input_text}],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")




