import requests
import os

API_ENDPOINT = "https://api.sheety.co/dbcf4328c6d08ff26795919a6d6a97b2/flightDeals/prices"
BEARER_TOKEN = str(os.environ.get("SHEETY_API_TOKEN"))

headers = {
    "Authorization": BEARER_TOKEN
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response_get = requests.get(url=API_ENDPOINT, headers=headers)
        data = response_get.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_data(self):
        for row in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": row['iataCode']
                }
            }
            response_put = requests.put(url=f"{API_ENDPOINT}/{row['id']}", json=new_data, headers=headers)
            print(response_put.text)
