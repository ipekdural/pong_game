from turtle import Turtle
from time import sleep

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.update_score()

    def update_score(self):
        self.clear()

        self.goto(-20, 230)
        self.write(f"{self.l_score} - {self.r_score}", align="center", font=("Courier", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()


