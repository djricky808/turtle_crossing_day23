from turtle import Screen
import time
from car_manager import CarManager
from player import Player
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
car = CarManager()

#Listen for the "Up" keypress to move the turtle north
screen.listen()
screen.onkey(fun=player.move_turtle,key="Up")

while game_is_running:
    i += 1
    time.sleep(0.1)
    car.move_car()
    screen.update()

screen.exitonclick()