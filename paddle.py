from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.location=location
        self.create_paddle()
    def create_paddle(self):
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.location)



    def go_up(self):
        y=self.ycor()
        self.goto(self.xcor(),y+20)

    def go_down(self):
        y=self.ycor()
        self.goto(self.xcor(),y-20)
