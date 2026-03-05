import random
from turtle import Turtle


class Food(Turtle):
    """Manages the food."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.penup()

    def respawn(self, snake_segments: list[Turtle]):
        """Moves the food to random location, avoids the snake's body."""
        touching_snake = True
        while touching_snake:
            self.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))
            for s in snake_segments:
                if self.distance(s) < 20:
                    break
            else:
                touching_snake = False