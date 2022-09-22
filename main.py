import time
from turtle import Turtle, Screen
import time
import pong
from pong import Bat, Ball, bat1_position, bat2_position, bat1, bat2, build_bat, build_ball, reset_bat
from scoreboard import Scores
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

score1 = Scores()
score2 = Scores()
score1.text(150,270)
score2.text(-150,270)

pong.build_line()
bat_1 = Bat(bat1_position, bat1)
bat_2 = Bat(bat2_position, bat2)
ball1 = Ball()
controls = [screen.onkey(bat_1.bat1_up, "Up"), screen.onkey(bat_1.bat1_down, "Down"), screen.onkey(bat_2.bat2_up, "w"),
            screen.onkey(bat_2.bat2_down, "s")]


game = True
screen.listen()


def reset_1():
    reset_bat(bat1_position, bat1)
    reset_bat(bat2_position, bat2)
    ball1.ball.goto(0,0)
    ball1.player2_turn()
    score1.score = ball1.player1_score
    score2.score = ball1.player2_score
    score1.text(150, 270)
    score2.text(-150, 270)
    time.sleep(0.5)


def reset_2():
    reset_bat(bat1_position, bat1)
    reset_bat(bat2_position, bat2)
    ball1.ball.goto(0, 0)
    ball1.player1_turn()
    score1.score = ball1.player1_score
    score2.score = ball1.player2_score
    score1.text(150, 270)
    score2.text(-150, 270)
    time.sleep(0.5)


ball1.who_goes_first()

while game:
    goal = ball1.check_ball()
    if goal == 1:
        reset_1()
    elif goal == 2:
        reset_2()
    goal = 0
    ball1.goal = goal
    ball1.move_ball()
    if ball1.player1_score == 10:
        game = False
        winner = Scores()
        winner.score = 'Player 1 Wins'
        winner.text(0,200)
    elif ball1.player2_score == 10:
        game = False
        winner = Scores()
        winner.score = 'Player 2 Wins'
        winner.text(0,200)



    screen.update()







screen.exitonclick()