from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import random
from score import Score
import time
screen = Screen()

screen.screensize(canvheight=600 , canvwidth=800)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)
first_paddle = Paddle(xcor=350, ycor=0)
second_paddle = Paddle(xcor=-350, ycor=0)

ball_object = Ball()
score_object = Score()

score_object.draw_lines()
score_object.write_on()

screen.listen()
screen.onkeypress(first_paddle.up, key="Up")
screen.onkeypress(first_paddle.down, key="Down")
screen.onkeypress(second_paddle.up, key="w")
screen.onkeypress(second_paddle.down, key="s")

is_game = True
def game_on():
    while is_game:
            ball_object.refresh()

            if abs(ball_object.ycor()) >= 290:
                ball_object.bounce()

            if abs(ball_object.xcor()) > 325:
                if first_paddle.distance(ball_object) < 55 or second_paddle.distance(ball_object) < 55:
                    ball_object.paddle_bounce()

            if ball_object.xcor() >= 370:
                score_object.left_score_board()
                ball_object.goto(0,0)
                game_on()
                screen.update()
                time.sleep(0.1)
                break

            elif ball_object.xcor() <= -370:
                score_object.right_score_board()
                ball_object.goto(0,0)
                game_on()
                screen.update()
                time.sleep(0.1)
                break

            screen.update()
            time.sleep(ball_object.move_speed)

game_on()
screen.exitonclick()