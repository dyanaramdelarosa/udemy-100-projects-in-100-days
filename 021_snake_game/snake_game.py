"""
Day 21 Project (Inheritance and List Slicing): Snake Game

This project completes the project on Day 20.
This part demonstrates inheritance with the scoreboard and food classes.
Also makes use of slicing in one of the game's functions.
"""

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

SCREEN_BORDER = [280, -280]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() in SCREEN_BORDER or snake.head.ycor() in SCREEN_BORDER:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
