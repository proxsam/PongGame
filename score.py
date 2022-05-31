from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 40, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0

    def draw_lines(self):
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(15, -300)
        self.setheading(90)

        for i in range(35):
            if i % 2 == 0:
                self.pendown()
                self.width(4)
                self.forward(20)
            else:
                self.penup()
                self.forward(20)

    def left_score_board(self):
        self.clear()
        self.left_score += 1
        self.draw_lines()
        self.write_on()


    def right_score_board(self):
        self.clear()
        self.right_score += 1
        self.draw_lines()
        self.write_on()


    def write_on(self):
        self.penup()
        self.goto(-20, 260)
        self.write(f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(50, 260)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT)
