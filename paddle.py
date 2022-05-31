from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.xcor = xcor
        self.ycor = ycor
        self.penup()
        self.shape("square")
        self.color("White")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed(-1)
        self.goto(x=self.xcor, y=self.ycor)

    def up(self):
        self.forward(25)

    def down(self):
        self.backward(25)









