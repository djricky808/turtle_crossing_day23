from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

root = screen.getcanvas().winfo_toplevel()
root.call('wm','attributes','.','-topmost','1')

game_is_running = True

while game_is_running:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()