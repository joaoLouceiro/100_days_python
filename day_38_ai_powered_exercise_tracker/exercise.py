from datetime import datetime

class Exercise:
    def __init__(self, name, duration, calories):
        self.name    = name
        self.duration= duration
        self.calories= calories
        self.date = datetime.today().strftime("%d/%m/%Y")
        self.time = datetime.now().strftime("%H:%M:%S")

    def to_string(self):
        print(f"date: {self.date}\n"
              f"name: {self.name}\n"
              f"duration: {self.duration}\n"
              f"calories: {self.calories}\n")
