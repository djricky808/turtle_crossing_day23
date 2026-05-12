from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    #Create a scoreboard that keeps track of which level the user is on.
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.setposition(-270, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"Level:{self.level}", move=False, align="left",font=FONT)