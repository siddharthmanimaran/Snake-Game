from turtle import Turtle

DISTANCE = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in DISTANCE:
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.goto(position)
            self.segment.append(t)

    def move(self):
        for segment in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[segment - 1].xcor()
            new_y = self.segment[segment - 1].ycor()
            self.segment[segment].goto(new_x, new_y)
        self.head.fd(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != UP:
            self.segment[0].seth(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].seth(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].seth(0)

    def add_segment(self, position):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segment.append(t)

    def extend(self):
        self.add_segment(self.segment[-1].position())
