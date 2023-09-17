import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from border import border_line
from score_board import Scoreboard
from time import sleep


def game():
    global score_tracer

    # Clear the screen
    screen.clear()

    # Recreate the border and set up the screen
    screen.tracer(0)
    border_line()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("PONG")

    # Create paddles, ball, and scoreboard
    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    score_board = Scoreboard()
    pen = Turtle()
    pen.color("blue")
    pen.hideturtle()
    pen.penup()

    # Set up key bindings
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    game_is_on = True

    while game_is_on:
        screen.update()
        ball.move()

        if score_board.l_score == 5:
            sleep(0.1)
            pen.goto(0, 80)
            pen.write("GAME OVER", align="center", font=("Courier", 40, "normal"))
            pen.goto(0, 60)
            pen.write("Press 'r' to restart", align="center", font=("Courier", 10, "normal"))
            pen.goto(-200, 0)
            pen.color("green")
            pen.write("You Win!", align="center", font=("Courier", 20, "normal"))
            pen.goto(200, 0)
            pen.color("red")
            pen.write("You Lose :(!", align="center", font=("Courier", 20, "normal"))
            game_is_on = False
        if score_board.r_score == 5:
            sleep(0.1)
            pen.goto(0, 80)
            pen.write("GAME OVER", align="center", font=("Courier", 40, "normal"))
            pen.goto(0, 60)
            pen.write("Press 'r' to restart", align="center", font=("Courier", 20, "normal"))
            pen.goto(200, 0)
            pen.color("green")
            pen.write("You Win!", align="center", font=("Courier", 20, "normal"))
            pen.goto(-200, 0)
            pen.color("red")
            pen.write("You Lose :(", align="center", font=("Courier", 20, "normal"))

            game_is_on = False
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        if (ball.distance(r_paddle) < 48 and ball.xcor() >= 325) or (
                ball.distance(l_paddle) < 48 and ball.xcor() <= -325):
            ball.bounce_x()
        if ball.xcor() > 380:  # right
            score_board.l_point()
            ball.restart()

        if ball.xcor() < -380:  # left
            score_board.r_point()
            ball.restart()

    # When the game is over, set up a listener for the "r" key to restart
    screen.onkey(game, "r")


# Set up the screen and initial game
screen = Screen()
score_tracer = 0
game()
screen.exitonclick()
