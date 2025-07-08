from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)
    def send_message(self, flight_data):
        message = self.client.messages.create(
            body=f"Low price alert! Only GBP {flight_data[2]} to fly from {flight_data[0]} to {flight_data[1]} on "
              f"{flight_data[3]}. Offer available until {flight_data[4]}.",
            from_= "whatsapp:+14155238886",
            to = "whatsapp:+447873757128",
        )
        print(message.sid)