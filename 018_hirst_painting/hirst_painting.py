"""
Day 18 Project (Turtle and GUI): Hirst Painting

This project uses the built-in module Turtle
to create our very own Hirst Painting
"""

import random
from turtle import Turtle, Screen
# import colorgram

# Extract colors from hirst painting
# Was not directly used because some colors were removed (close to black or white colors)
# colors = colorgram.extract("image.png", 30)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append(tuple(color.rgb))
# print(rgb_colors)

# Set colors extracted from Hirst painting
color_list = [
    (116, 175, 204),
    (31, 112, 167),
    (233, 208, 101),
    (235, 56, 102),
    (247, 70, 43),
    (32, 177, 116),
    (247, 153, 200),
    (148, 54, 110),
    (199, 181, 14),
    (219, 139, 185),
    (8, 143, 92),
    (11, 177, 205),
    (22, 46, 140),
    (96, 208, 184),
    (147, 69, 47),
    (250, 164, 156),
    (139, 213, 226),
    (15, 44, 69),
    (7, 54, 30),
    (133, 218, 194),
    (132, 33, 91),
    (132, 36, 25),
    (2, 114, 69),
    (50, 37, 52),
]

# Setup screen
screen = Screen()
screen.colormode(255)
screen.setworldcoordinates(0, 0, 500, 500)

# Setup turtle
pointer = Turtle()
pointer.speed("fastest")
pointer.penup()

# draw painting
for y in range(20, 500, 50):
    for x in range(20, 500, 50):
        pointer.setx(x)
        pointer.sety(y)
        pointer.dot(40, random.choice(color_list))

screen.exitonclick()
