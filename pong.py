from turtle import Turtle, Screen
import time
import random


bat1_position = [(280, -20), (280, 0), (280, 20)]
bat2_position = [(-280, -20), (-280, 0), (-280, 20)]
bat1 = []
bat2 = []


def build_bat(bat_position, bat):
    """Builds bat by placing Turtle class objects in the specified positions, then stores in a list of objects"""
    for position in bat_position:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        bat.append(new_segment)


def reset_bat(bat_position, bat):
    length = len(bat_position)
    for n in range(0, length):
        bat[n].goto(bat_position[n])


def build_line():
    t = Turtle('square')
    t.color('white')
    t.shapesize(30, 0.1)
    t.goto(0, 0)


def build_ball():
    ball = Turtle('square')
    ball.color('white')
    ball.shapesize(0.5)
    ball.penup()
    ball.goto(0,0)
    return ball


class Bat:
    def __init__(self, bat_position, bat):
        build_bat(bat_position, bat)
        self.length = 0

    """The following 4 methods define how the bat objects will move up and down. As the bat variables are lists of 
    turtle objects, each object must move individually"""
    def bat1_up(self):
        self.length = len(bat1)
        for n in range(0, self.length - 1):
            x = bat1[n + 1].xcor()
            y = bat1[n + 1].ycor()
            bat1[n].goto(x, y)
        bat1[self.length - 1].setheading(90)
        bat1[self.length - 1].forward(20)


    def bat1_down(self):
        self.length = len(bat1)
        for n in range(self.length - 1, 0, - 1):
            x = bat1[n - 1].xcor()
            y = bat1[n - 1].ycor()
            bat1[n].goto(x, y)
        bat1[0].setheading(270)
        bat1[0].forward(20)


    def bat2_up(self):
        self.length = len(bat2)
        for n in range(0, self.length - 1):
            x = bat2[n + 1].xcor()
            y = bat2[n + 1].ycor()
            bat2[n].goto(x, y)
        bat2[self.length - 1].setheading(90)
        bat2[self.length - 1].forward(20)


    def bat2_down(self):
        self.length = len(bat2)
        for n in range(self.length - 1, 0, - 1):
            x = bat2[n - 1].xcor()
            y = bat2[n - 1].ycor()
            bat2[n].goto(x, y)
        bat2[0].setheading(270)
        bat2[0].forward(20)


class Ball:
    def __init__(self):
        """Builds and configures the ball"""
        self.ball = build_ball()
        self.heading = self.ball.heading()
        self.xcor = self.ball.xcor()
        self.ycor = self.ball.ycor()
        self.player1_score = 0
        self.player2_score = 0
        self.goal = 0


    def who_goes_first(self):
        if random.randint(1, 2) == 1:
            self.player1_turn()
        else:
            self.player2_turn()
        self.heading = self.ball.heading()

    """The next 2 methods define how the ball's direction would be randomly set after a player has scored"""
    def player1_turn(self):
        ranges = random.choice([(10, 50), (-50, -10)])
        player1 = random.randrange(ranges[0], ranges[1])
        self.ball.setheading(player1)


    def player2_turn(self):
        ranges = random.choice([(130, 170), (190, 230)])
        player2 = random.randrange(ranges[0], ranges[1])
        self.ball.setheading(player2)


    def move_ball(self):
        self.ball.forward(19)
        time.sleep(0.1)


    def rebound(self):
        """Sets conditions to determine the rebound direction of the ball"""
        if 0 <= self.heading <= 90 and self.ycor >= 300:
            self.ball.setheading(360 - self.heading)
        elif 90 < self.heading <= 180 and self.ycor >= 300:
            self.ball.setheading(270 - (self.heading - 90))
        elif 180 < self.heading <= 270 and self.ycor <= -300:
            self.ball.setheading(180 - (self.heading - 180))
        elif 270 < self.heading <= 360 and self.ycor <= -300:
            self.ball.setheading(self.heading - 270)

    def bat1_rebound(self):
        if 0 <= self.heading <= 90:
            self.ball.setheading(180 - self.heading)
        elif 270 < self.heading <= 360:
            self.ball.setheading(270 - (self.heading - 270))

    def bat2_rebound(self):
        if 90 < self.heading <= 180:
            self.ball.setheading(90 - (self.heading - 90))
        elif 180 < self.heading <= 270:
            self.ball.setheading(360 - (self.heading - 180))

    def check_ball(self):
        self.xcor = self.ball.xcor()
        self.ycor = self.ball.ycor()
        self.heading = self.ball.heading()
        if self.ycor >= 300 or self.ycor <= -300:
            self.rebound()
        if self.xcor >= 300:
            self.player2_score += 1
            print('Player 2 scored')
            self.goal = 2
            return self.goal
        elif self.xcor <= -300:
            self.player1_score += 1
            print('Player 1 scored')
            self.goal = 1
            return self.goal

        for n in bat1:
            if n.xcor() - 10 <= self.xcor <= n.xcor() + 10 and n.ycor() - 10 <= self.ycor <= n.ycor() + 10:
                self.bat1_rebound()
                break
        for n in bat2:
            if n.xcor() - 10 <= self.xcor <= n.xcor() + 10 and n.ycor() - 10 <= self.ycor <= n.ycor() + 10:
                self.bat2_rebound()
                break



