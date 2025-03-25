import requests
from os import environ as env
from datetime import date, timedelta

from requests import HTTPError

API_URL = "https://test.api.amadeus.com"
API_KEY = env["AM_KEY"]
API_SECRET = env["AM_SECRET"]

class CityNotFoundError(Exception):
    pass

class FlightSearch:

    def __init__(self):
        self.token = {}

    def req_wrapper(self, method, url, retries=1, **kwargs) -> requests.Response:
        if retries < 0:
            raise ConnectionAbortedError("Maximum number of retries exceeded")

        headers = self.token
        if kwargs.get("headers") is not None:
            headers.update(kwargs.get("headers"))

        try:
            req = method(url, kwargs, headers=headers)
            req.raise_for_status()
            return req
        except HTTPError:
            if req.status_code == 401:
                self.get_token()
                retries -= 1
                return self.req_wrapper(method=method, url=url, retries=retries, kwargs=kwargs)
            else:
                raise

    def get_iata(self, cityName):
        print(f"# Getting IATA Code for {cityName}")
        url = f"{API_URL}/v1/reference-data/locations/cities?keyword={cityName}&max=1"
        req = self.req_wrapper(method=requests.get, url=url)
        try:
            return req.json()["data"][0]["iataCode"]
        except KeyError:
            print(f"No city found for {cityName}")

    def get_flight_offer(self, origin, destination, limit, is_direct):
        print(f"# Getting flight offers for {destination}")
        tomorrow = date.today() + timedelta(days=30)
        url = f"{API_URL}/v2/shopping/flight-offers?originLocationCode={origin}&destinationLocationCode={destination}&departureDate={tomorrow}&adults=1&nonStop={is_direct}&currencyCode=EUR&maxPrice={limit}"
        req = self.req_wrapper(method=requests.get, url=url)
        return req.json()["data"]

    def get_token(self):
        print("# # Getting a new token")
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET
        }
        req = requests.post(url=f"{API_URL}/v1/security/oauth2/token", data=body, headers=header)
        req.raise_for_status()
        self.token = {
            'Authorization': f'Bearer {req.json()["access_token"]}'
        }

        