from turtle import Turtle
import random

CARS = ["./photos/ambulance.gif", "./photos/car.gif", "./photos/greentruck.gif", "./photos/minibus.gif", "./photos/taxi.gif", "./photos/whitetruck.gif", "./photos/redcar.gif"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class Cars:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle(random.choice(CARS))
            new_car.penup()
            random_y = random.randint(-245, 250)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
