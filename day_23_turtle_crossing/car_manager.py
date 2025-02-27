import random
from turtle import Turtle
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_SIZE = 240
STARTING_NUMBER_OF_CARS = 15

def get_random_coord():
    return (random.randint(0, SCREEN_SIZE // 20) * random.choice([-1, 1])) * 20

class CarManager:
    def __init__(self):
        self.cars = []
        for _ in range(0, STARTING_NUMBER_OF_CARS):
            self.add_car(get_random_coord())
        self.movement_speed = STARTING_MOVE_DISTANCE

    def add_car(self, x_coord=320):
        start_coord = (x_coord, get_random_coord())
        color = random.choice(COLORS)
        self.cars.append(Car(coord=start_coord, color=color))

    def move_cars(self):
        self.random_car_generator()
        for car in self.cars:
            if car.xcor() > 320:
                self.cars.remove(car)
            car.move(self.movement_speed)

    def random_car_generator(self):
        if random.random() < 0.2:
            self.add_car()

    def increase_speed(self):
        self.movement_speed += MOVE_INCREMENT

    def detect_collision(self, player):
        for c in self.cars:
            if c.detect_collision(player):
                return True
        return False
