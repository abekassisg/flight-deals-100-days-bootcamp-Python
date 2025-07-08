#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

DataManagerObject = DataManager()
data_manager = DataManagerObject.get_destination_data()

FlightSearchObject = FlightSearch()
flight_search = FlightSearchObject.flight_search(data_manager)
flight_search_query_params = FlightSearchObject.query_params

FlightData = FlightData()
flight_data = FlightData.format_message(flight_search, flight_search_query_params)

NotificationManager = NotificationManager()
NotificationManager.send_message(flight_data)





