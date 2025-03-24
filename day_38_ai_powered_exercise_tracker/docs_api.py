import requests
from os import environ as env

from exercise import Exercise

APP_URL = f'https://api.sheety.co/{env["SHEETY_URL"]}'
TOKEN = "MYSECRETTOKEN"

def post(exercise: Exercise):
    body = {
        "workout": {
            "date": exercise.date,
            "time": exercise.time,
            "exercise": exercise.name,
            "duration": exercise.duration,
            "calories": exercise.calories

        }
    }
    req = requests.post(APP_URL, json=body, auth=(env["SHEETY_USER"],env["SHEETY_PASS"]))
    req.raise_for_status()
    print(req)