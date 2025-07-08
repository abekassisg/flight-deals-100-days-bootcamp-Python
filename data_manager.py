import requests

# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.GOOGLE_SHEET_ENDPOINT = "https://api.sheety.co/2bd7fb15c99895dd71014d15172af727/flightDeals/prices"
    def get_destination_data(self):
        response = requests.get(self.GOOGLE_SHEET_ENDPOINT)
        data_json = response.json()
        print(f"data-manager: {data_json}")
        self.trips_dictionary = {
            entry["iataCode"]: entry["lowestPrice"]
            for entry in data_json["prices"]
        }
        return self.trips_dictionary