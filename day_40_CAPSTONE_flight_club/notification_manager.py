import os
from twilio.rest import Client
import smtplib

from flight_data import Flight

TWILIO_ACCOUNT_ID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]

SMTP_PASS = os.getenv("SMTP_PASS")
SMTP_MAIL = os.getenv("SMTP_MAIL")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")

def make_notification(flight: Flight):
    return (f"We found a flight for you!\n"
            f"{flight}")


def make_email(first_name, last_name, flight_list):
    parsed_list = ""
    for f in flight_list:
        parsed_list += f"*******\n{f}\n\n"
    return (f"Hello, {first_name} {last_name}\n"
            f"We found some cool flights for you:\n\n"
            f"{parsed_list}")


def get_smtp_connection():
    connection = smtplib.SMTP(host=SMTP_HOST, port=int(SMTP_PORT))
    connection.starttls()
    connection.login(user=SMTP_MAIL, password=SMTP_PASS)
    return connection


class NotificationManager:
    def __init__(self):
        self.smtp_connection = get_smtp_connection()
        self.twilio_client = Client(TWILIO_ACCOUNT_ID, TWILIO_AUTH_TOKEN)


    def send_text_message(self, body):
        message = self.twilio_client.messages.create(
            to="***REMOVED***",
            from_="***REMOVED***",
            body=body,
        )
        print(message.body)

    def send_email(self, to_email, message):
        self.smtp_connection.sendmail(from_addr=SMTP_MAIL, to_addrs=to_email, msg=f"Subject: Flight Club\n\n{message}")
