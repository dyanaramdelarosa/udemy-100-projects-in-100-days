from enum import Enum
from turtle import Turtle

MOVE_DISTANCE = 20


class Direction(Enum):
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0


class Snake:
    def __init__(self):
        self.segments: [list[Turtle]] = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            new_heading = self.segments[seg_num - 1].heading()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[seg_num].setheading(new_heading)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self) -> None:
        if self.head.heading() != Direction.DOWN.value:
            self.head.setheading(Direction.UP.value)

    def down(self) -> None:
        if self.head.heading() != Direction.UP.value:
            self.head.setheading(Direction.DOWN.value)

    def left(self) -> None:
        if self.head.heading() != Direction.RIGHT.value:
            self.head.setheading(Direction.LEFT.value)

    def right(self) -> None:
        if self.head.heading() != Direction.LEFT.value:
            self.head.setheading(Direction.RIGHT.value)
