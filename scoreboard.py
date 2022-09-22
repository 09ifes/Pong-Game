from turtle import Turtle, Screen

"""Configures the displaying of scores/text on screen"""
class Scores(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def text(self, x, y):
        self.clear()
        self.penup()
        self.goto(x, y)
        self.color('white')
        self.write(f'{self.score}', True, align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def end(self):
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.write(f'Game Over! Your Score: {self.score}', True, align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()

