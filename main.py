import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard

# Set up screen and add shape images

screen = Screen()
screen.title("Cross Road")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.addshape("turtle.gif")
screen.addshape("redcar.gif")
screen.addshape("car.gif")
screen.addshape("taxi.gif")
screen.addshape("minibus.gif")
screen.addshape("whitetruck.gif")
screen.addshape("greentruck.gif")
screen.addshape("ambulance.gif")

player = Player()
cars = Cars()
scoreboard = Scoreboard()

# Move turtle with Up keys

screen.listen()
screen.onkeypress(player.go_up, "Up")

is_game_on = True

while is_game_on:
    time.sleep(0.12)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    # Detect collision with cars

    for car in cars.all_cars:
        if car.distance(player) < 25:
            is_game_on = False
            scoreboard.game_over()

    # Detect successful crossing and level up

    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        scoreboard.increase_level()

screen.exitonclick()
