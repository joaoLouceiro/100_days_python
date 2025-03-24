import requests
from os import environ as env

APP_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": env["APP_ID"],
    "x-app-key": env["API_KEY"],
    "x-remote-user-id": "0"
}

def post(query):
    body = {"query": query}
    req = requests.post(url=APP_URL, headers=headers, json=body)
    req.raise_for_status()
    return req
