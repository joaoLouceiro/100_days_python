import os
from twilio.rest import Client

from flight_data import Flight

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

class NotificationManager:

    @staticmethod
    def make_notification(flight: Flight):
        return (f"Found a flight for you!\n"
                f"{flight}")

    @staticmethod
    def send_text_message(body):
        message = client.messages.create(
            to="***REMOVED***",
            from_="***REMOVED***",
            body=body,
        )
        print(message.body)

    

