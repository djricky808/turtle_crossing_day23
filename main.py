from turtle import Screen
import time
from car_manager import CarManager
from player import Player, FINISH_LINE_Y
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

CAR_GENERATION_RATE = 6
i = 0

root = screen.getcanvas().winfo_toplevel()
root.call('wm','attributes','.','-topmost','1')

game_is_running = True

player = Player()
cars = []

#Listen for the "Up" keypress to move the turtle north
screen.listen()
screen.onkey(fun=player.move_turtle,key="Up")

while game_is_running:
    i += 1
    time.sleep(0.1)
    if i == CAR_GENERATION_RATE:
        car = CarManager()
        cars.append(car)
        i = 0
    for car in cars:
        car.move_car()
    #Detect when the player has reached the top of the screen
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_position()
    screen.update()

screen.exitonclick()