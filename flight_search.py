import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("FLIGHT_SEARCH_AMADEUS_API_KEY")
API_SECRET = os.getenv("FLIGHT_SEARCH_AMADEUS_API_SECRET")
print(f"Loaded API_KEY: {API_KEY}")
POST_REQUEST_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
GRANT_TYPE = "client_credentials"
ORIGIN_CODE = "LON"
ACCESS_TOKEN = "wgmf7PlGXt7yxKTacgiGvEOfUu96"

headers = {"Content-Type" : "application/x-www-form-urlencoded"}

data = {
    "grant_type" : GRANT_TYPE,
    "client_id": API_KEY,
    "client_secret": API_SECRET,
}

#response = requests.post(url=POST_REQUEST_ENDPOINT, headers=headers, data=data)
#print(response.text)

class FlightSearch: #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.get_request_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        #TEST self.code_and_price_dict = {
        #    'PAR': 1000 * 0.85,
        #    'TYO': 30 * 0.85,
        #    'HKG': 22 * 0.85,
        #    'NYC': 78 * 0.85,
        #    'SFO': 1500 * 0.85
        #}
        self.headers_auth = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
        }
        self.responses = []
        self.result = []
        self.query_params = {}
        self.get_flight_response = ""
    def flight_search(self, city_dictionary):
        code_and_price_dict = city_dictionary
        print("flight_search: Running search loop...")
        i = 1
        while i <= 180:
            for city in code_and_price_dict.items():
                date_to_check = datetime.date.today() + datetime.timedelta(days=i)
                self.query_params = {
                    "originLocationCode": ORIGIN_CODE,
                    "destinationLocationCode": city[0],
                    "departureDate": str(date_to_check),
                    "adults": 1,
                    "maxPrice": int(city[1] * 0.85)
                }
                print(f"flight_search : this is the current result: {self.query_params}")
                self.get_flight_response = requests.get(url=self.get_request_endpoint, headers=self.headers_auth, params=self.query_params)
                if self.get_flight_response.status_code != 200:
                    print(self.get_flight_response.text)
                json_data = self.get_flight_response.json()
                print(f"Number of offers in json_data: {json_data["meta"]["count"]}")
                if json_data["meta"]["count"] > 0:
                    list_of_prices = [item["price"]["total"] for item in json_data["data"]]
                    print(f"flight_search: These are all prices from the offer: {list_of_prices}")
                    print(f"flight_search: This is how many prices I am comparing: {len(list_of_prices)}")
                    min_price = min(float(item["price"]["total"]) for item in json_data["data"])
                    print(f"flight_search: Minimum price in response: {min_price}")
                    matches = [item for item in json_data["data"] if float(item["price"]["total"]) == min_price]
                    self.result.extend(matches)
                    print(f"flight_search: Winning result: {self.result}")
                    return self.result
                else:
                    i += 1

#flight_object = FlightSearch()
#flight_object.flight_search()