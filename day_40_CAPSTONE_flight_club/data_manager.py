from os import environ as env
from requests import get, put

SHEET_GUID=env["SH_GUID"]
SHEET_TOKEN=env["SH_TOKEN"]

API_URL = f"https://api.sheety.co/{SHEET_GUID}/flightDeals"
HEADERS = {
    "Authorization": f"Basic {SHEET_TOKEN}"
}

class DataManager:
    @staticmethod
    def get_prices_data():
        url = f"{API_URL}/prices"
        req = get(url=url, headers=HEADERS)
        req.raise_for_status()
        return req.json()["prices"]

    @staticmethod
    def update_price_data(body):
        url = f"{API_URL}/prices"
        req =put(f"{url}/prices/{body['id']}", headers=HEADERS, json={"price":body})
        req.raise_for_status()
        return req

    @staticmethod
    def get_users_data():
        url = f"{API_URL}/users"
        req = get(url=url, headers=HEADERS)
        req.raise_for_status()
        return req.json()["users"]

