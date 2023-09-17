from turtle import Turtle
from time import sleep
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 0)
        self.color("blue")
        self.shape("circle")

        self.penup()
        self.x_move = 0.5
        self.y_move = 0.5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def restart(self):
        self.goto(0,0)
        sleep(0.2)
        self.bounce_x()
    def speed_up(self):
        self.y_move*=2