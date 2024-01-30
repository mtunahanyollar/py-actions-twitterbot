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
def currencies():
    import requests
    import json
    baseUrl = "https://hasanadiguzel.com.tr/api/kurgetir"
    response = requests.get(baseUrl)
    data = ""
    euro_values = {
        "BanknoteBuying": "",
        "BanknoteSelling": ""
    }

    usd_values = {
        "BanknoteBuying": "",
        "BanknoteSelling": ""
    }
    if response.status_code == 200:
    # Print the response content (the data returned by the API)
        #print(response.json())  # Assuming the response is in JSON format
        json_string = json.dumps(response.json(), indent=2)
        data = json.loads(json_string)
        for currency in data["TCMB_AnlikKurBilgileri"]:
            if currency["Isim"] == "EURO":
                euro_values["BanknoteBuying"] = str(currency["BanknoteBuying"])
                euro_values["BanknoteSelling"] = str(currency["BanknoteSelling"])
            elif currency["Isim"] == "ABD DOLARI":
                usd_values["BanknoteBuying"] = str(currency["BanknoteBuying"])
                usd_values["BanknoteSelling"] = str(currency["BanknoteSelling"])


    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print(response.text)  # Print the response content in case of an error

    # Print the extracted values
    #print("Kursunsuz_95(Excellium95)_TL/lt:", values[0])
    #print("Motorin(Eurodiesel)_TL/lt:", values[1])
    return euro_values, usd_values
# Auth
tt = tweepy.Client(
    #Consumer Keys
    consumer_key= os.environ['CONSUMER_API_KEY'],
    consumer_secret= os.environ['CONSUMER_API_SECRET'],
    # Access Token and Secret
    access_token= os.environ['ACCESS_TOKEN'],
    access_token_secret= os.environ['ACCESS_TOKEN_SECRET'])

# ## Defining Functions
    
gasolineValues = gasoline("ISTANBUL")
euro_values, usd_values = currencies()
finalText = "L o L :  \n"+ "Kursunsuz_95(Excellium95)_TL/lt " + gasolineValues[0] + "\n" + "Motorin(Eurodiesel)_TL/lt " + gasolineValues[1]
finalText = finalText + "\n\n" + "USD ALIŞ: " + usd_values["BanknoteBuying"] + "\nUSD SATIŞ: " + usd_values["BanknoteSelling"]+ "\n\nEURO ALIŞ: " + euro_values["BanknoteBuying"] + "\nEURO SATIŞ: " +  euro_values["BanknoteSelling"]
print(finalText)
tt.create_tweet(text= finalText)

