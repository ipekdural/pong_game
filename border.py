from turtle import Turtle,Screen
screen=Screen()
screen.tracer(0)
def border_line():
    border=Turtle()
    border.hideturtle()
    border.pensize(20)
    border.penup()
    border.color("red")
    border.goto(400,300)
    border.pendown()
    border.goto(-400,300)
    border.penup()
    border.goto(-400,-295)
    border.pendown()
    border.goto(400,-295)
    screen.update()