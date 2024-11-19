import random
from turtle import Turtle, Screen


def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


screen = Screen()
screen.colormode(255)
turtle = Turtle()
turtle.speed("fastest")
for _ in range(0, 36):
    turtle.color(random_color())
    turtle.circle(50)
    turtle.left(10)


# from turtle import Turtle, Screen
# import random
#
# point = Turtle()
#
# for sides in range(3, 10):
#     angle = 360/sides
#     for _ in range(sides):
#         point.fd(100)
#         point.right(angle)

# colors = ["red", "green", "blue", "brown"]
# turtles: list[Turtle] = [Turtle() for _ in range(4)]
# for turtle in turtles:
#     turtle.shape("turtle")
#     turtle.color(colors.pop())
#
# for _ in range(50):
#     for turtle in turtles:
#         turtle.setheading(random.choice([0, 90, 180, 270]))
#         turtle.forward(20)
# if turtle.isdown():
#     turtle.up()
# else:
#     turtle.down()

# tim.fd(100)
# tom.left(90)
# tom.fd(100)
# tam.right(90)
# tam.fd(100)
# Draw square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# tim.home()
# tim.dot()
# tim.fd(50); tim.dot(20, "blue"); tim.fd(50)
# tim.position()
# tim.heading()

screen = Screen()
screen.exitonclick()
