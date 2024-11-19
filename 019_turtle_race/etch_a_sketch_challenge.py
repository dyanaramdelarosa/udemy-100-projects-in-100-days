"""
Challenge: Build and Etch-a-Sketch program
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def rotate_counterclockwise():
    tim.right(10)


def rotate_clockwise():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
tim.shape("turtle")
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_clockwise)
screen.onkey(key="d", fun=rotate_counterclockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
