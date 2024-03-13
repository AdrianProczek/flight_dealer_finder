import requests
from flight_data import FlightData
import os

API_ENDPOINT = "https://api.tequila.kiwi.com"
API_KEY = str(os.environ.get("KIWI_API_KEY"))

headers = {
    "apikey": API_KEY
}


class FlightSearch:

    def search_iata_code(self, city):
        parameters = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=f"{API_ENDPOINT}/locations/query", params=parameters, headers=headers)
        code = response.json()["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city, tomorrow, plus_6_months):

        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city,
            "date_from": tomorrow,
            "date_to": plus_6_months,
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=f"{API_ENDPOINT}/v2/search", params=parameters, headers=headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: {flight_data.price}")
        return flight_data

