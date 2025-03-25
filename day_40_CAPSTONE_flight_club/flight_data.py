def get_flights_below_limit(flights: list, limit: float):
    return [f for f in flights if f.price < limit]

def get_cheapest_flight(flights: list):
    return min(flights)

class Flight:
    def __init__(self, origin, destination, date, price):
        self.origin = origin
        self.destination = destination
        self.date = date
        self.price = float(price)

    def __repr__(self):
        return f"\tOrigin: {self.origin}\n\tDestination: {self.destination}\n\tDate: {self.date}\n\tPrice: {self.price}€"

    def __lt__(self, other):
        return self.price < other.price