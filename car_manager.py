from turtle import Turtle
import random

COLORS = ["red","orange","yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_ZONE = (-230, 230)

class CarManager(Turtle):
    #Create cars that are 20px high by 40px wide that are randomly generated along the y-axis.
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setposition(x=270, y=random.randint(CAR_ZONE[0],CAR_ZONE[1]))
    #No cars should be generated in the top and bottom 50px of the screen (Turtle safe zone)
    #Move the cars from the right edge to the left edge of the screen
    #Generate a new car only every time 6th time the game loop runs
