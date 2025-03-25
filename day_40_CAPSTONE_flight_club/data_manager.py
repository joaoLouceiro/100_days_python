from os import environ as env
from requests import get, put

SHEET_GUID=env["SH_GUID"]
SHEET_TOKEN=env["SH_TOKEN"]

API_URL = f"https://api.sheety.co/{SHEET_GUID}/flightDeals/prices"
HEADERS = {
    "Authorization": f"Basic {SHEET_TOKEN}"
}

class DataManager:
    @staticmethod
    def get_sheet_data():
        req = get(url=API_URL, headers=HEADERS)
        req.raise_for_status()
        return req.json()["prices"]

    @staticmethod
    def update_row_data(body):
        req =put(f"{API_URL}/{body['id']}", headers=HEADERS, json={"price":body})
        req.raise_for_status()
        return req
