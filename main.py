import time
from turtle import Screen
from pongball import Ball
from pongpaddle import Pongpaddle
from scoreboard import Scoreboard

#Code to initialize the GUI screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game - G Edition")
screen.tracer(0)

#Create the object used for this game from their associated class
r_paddle = Pongpaddle((350, 0))
l_paddle = Pongpaddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the top of the wall.
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()
        #print(ball.ycor())

    # Detect collision with r_paddle and l_paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        #print(f"Ball hit paddle at {ball.xcor()}")

    #Detect if the ball has gone past the r_paddle.
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.r_point()

    # Detect if the ball has gone past the l-paddle.
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.l_point()

    # game_is_on = False
    # print(ball.xcor())


screen.exitonclick()
