from turtle import Turtle


class Snake:
    """Creates the snake and handles its controls."""

    def __init__(self):
        self.head = Turtle("square")
        self.head.shapesize(0.9, 0.9)
        self.head.color("limegreen")
        self.head.penup()

        self._s1= Turtle("square")
        self._s1.shapesize(0.9, 0.9)
        self._s1.penup()
        self._s1.color("limegreen")
        self._s1.goto(-20, 0)

        self._s2 = Turtle("square")
        self._s2.shapesize(0.9, 0.9)
        self._s2.penup()
        self._s2.color("limegreen")
        self._s2.goto(-40, 0)

        self._key_press = 0
        self.snake_segments = [self.head, self._s1, self._s2]

    def right(self):
        if self.head.heading() != 180 and self._key_press == 0:
            self.head.setheading(0)
            self._key_press += 1

    def left(self):
        if self.head.heading() != 0 and self._key_press == 0:
            self.head.setheading(180)
            self._key_press += 1

    def up(self):
        if self.head.heading() != 270 and self._key_press == 0:
            self.head.setheading(90)
            self._key_press += 1

    def down(self):
        if self.head.heading() != 90 and self._key_press == 0:
            self.head.setheading(270)
            self._key_press += 1

    def move(self):
        """Moves the snake forward and unlocks controls for the next tick."""
        if self._key_press != 0:
            self._key_press = 0

        for i in range(len(self.snake_segments)-1, 0, -1):
            self.snake_segments[i].goto(self.snake_segments[i-1].xcor(), self.snake_segments[i-1].ycor())

        self.head.forward(20)

    def new_segments(self):
        """Handles new segments."""
        self.new_seg = Turtle("square")
        self.new_seg.shapesize(0.9, 0.9)
        self.new_seg.penup()
        self.new_seg.color("limegreen")
        self.new_seg.goto(self.snake_segments[-1].xcor(), self.snake_segments[-1].ycor())
        self.snake_segments.append(self.new_seg)