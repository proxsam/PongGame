from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("Blue")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.move_speed = 0.02
        self.goto(0, 0)
        self.setheading(random.randint(46, 80))

    def refresh(self):
        self.forward(12)
        self.move_speed = 0.02

    def bounce(self):
        angle = self.heading()
        new_angle = int(360 - angle)
        self.setheading(new_angle)
        self.refresh()

    def paddle_bounce(self):
        angle = self.heading()
        new_angle = int(180 - angle)
        self.setheading(new_angle)
        self.refresh()


