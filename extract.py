import json
import requests
def extract_data():
    url = "https://dummyjson.com/users"
    response = requests.get(url)
    if response.status_code==200:
        print("connected to the API successfully")
        data=response.json()
        print("data extracted successfully")
    return data

   