#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time

import flight_data as fd
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch

dm = DataManager()
fs = FlightSearch()
destinations = dm.get_prices_data()
users = dm.get_users_data()

# origin = input("Where do you want to leave from? ")
# origin_iata = fs.get_iata(origin)
# print(f"\tOrigin set as {origin_iata}")

origin_iata = "OPO"
all_flights = []

for destination in destinations:
    iataCode = destination.get("iataCode")
    if iataCode is None or iataCode == '':
        destination["iataCode"] = fs.get_iata(destination["city"])
        dm.update_price_data(destination)
    f_data =fs.get_flight_offer(origin=origin_iata, destination=destination["iataCode"], limit=destination["lowestPrice"])
    if len(f_data) == 0:
        print(f"\tNo flights found for {destination['city']}")
    else:
        flights = [fd.Flight(origin="OPO", destination=destination.get("iataCode"), date=item["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0], price=item["price"]["total"]) for item in f_data]
        cheapest = fd.get_cheapest_flight(flights)
        all_flights.append(cheapest)
        print(NotificationManager.make_notification(cheapest))
        # NotificationManager().send_whatsapp_message(NotificationManager().make_notification(cheapest))

    time.sleep(0.5)

if len(all_flights) > 0:
    for user in users:
        (NotificationManager.make_email(user["primeiroNome"], user["ultimoNome"], all_flights))
