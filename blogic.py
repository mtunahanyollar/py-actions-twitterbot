import os
import tweepy

def gasoline(city):
    import requests
    import json
    baseUrl = "https://hasanadiguzel.com.tr/api/akaryakit/sehir=" + city
    response = requests.get(baseUrl)
    data = ""
    values = []
    if response.status_code == 200:
    # Print the response content (the data returned by the API)
        #print(response.json())  # Assuming the response is in JSON format
        json_string = json.dumps(response.json(), indent=2)
        data = json.loads(json_string)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print(response.text)  # Print the response content in case of an error
    
    for key, inner_dict in data["data"].items():
        values.append(inner_dict["Kursunsuz_95(Excellium95)_TL/lt"])
        values.append(inner_dict["Motorin(Eurodiesel)_TL/lt"])

    # Print the extracted values
    #print("Kursunsuz_95(Excellium95)_TL/lt:", values[0])
    #print("Motorin(Eurodiesel)_TL/lt:", values[1])
    return values
# Auth
tt = tweepy.Client(
    #Consumer Keys
    consumer_key= os.environ['CONSUMER_API_KEY'],
    consumer_secret= os.environ['CONSUMER_API_SECRET'],
    # Access Token and Secret
    access_token= os.environ['ACCESS_TOKEN'],
    access_token_secret= os.environ['ACCESS_TOKEN_SECRET'])
  
# ## Defining Functions
    
values = gasoline("ISTANBUL")
finalText = "Kagithane Akaryakit Fiyatlari: \n"+ "Kursunsuz_95(Excellium95)_TL/lt " + values[0] + "\n" + "Motorin(Eurodiesel)_TL/lt " + values[1]
print(finalText)
tt.create_tweet(text= finalText)

