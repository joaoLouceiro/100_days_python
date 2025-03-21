import requests

API_KEY = <redacted>
LATITUDE = 40.2287599
LONGITUDE = -8.4162744
params = {
    "lat" : LATITUDE,
    "lon" : LONGITUDE,
    "appid" : API_KEY,
    "cnt": 4

}

def will_be_raining() -> bool:
    for forecast in forecast_list:
        for weather in forecast["weather"]:
            if weather["id"] < 700:
                return True
    return False


req = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
req.raise_for_status()
forecast_list = req.json()["list"]

print(will_be_raining())
