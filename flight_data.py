from datetime import datetime
from flight_search import FlightSearch

flight_search = FlightSearch()

class FlightData:
    def __init__(self):
        self.cheapest_flight_info = []
    def format_message(self, search_result, query_params):
        response = search_result
        if float(response[0]["price"]["total"]) < float(query_params["maxPrice"]):
            self.cheapest_flight_info.append(response[0]["itineraries"][0]["segments"][0]["departure"]["iataCode"])
            segments = response[0]["itineraries"][0]["segments"]
            self.cheapest_flight_info.append(segments[-1]["arrival"]["iataCode"])
            self.cheapest_flight_info.append(response[0]["price"]["total"])
            dt = datetime.strptime(response[0]["itineraries"][0]["segments"][0]["departure"]["at"], "%Y-%m-%dT%H:%M:%S")
            formatted = dt.strftime("%Y-%m-%d")
            self.cheapest_flight_info.append(formatted)
            self.cheapest_flight_info.append(response[0]["lastTicketingDate"])
            print(f"flight_data: This is the cheapest_flight_info: {self.cheapest_flight_info}")
            return self.cheapest_flight_info