from turtle import Turtle

STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    #Create the turtle player
    def __init__(self):
        super().__init__()
        self.reset_position()

    def reset_position(self):
        self.position = (0, -200)

    def move_turtle(self):
        self.position = (0, self.ycor()+ MOVE_DISTANCE)
