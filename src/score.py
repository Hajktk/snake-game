import os
from turtle import Turtle


class Score(Turtle):
    """Displays and updates the score and shows game over message."""

    def __init__(self):
        super().__init__()
        self._current_score: int = 0
        self._high_score: int = 0
        self.hideturtle()
        self.penup()
    
    def _update_high_score(self):
        file_path = os.path.join(os.path.dirname(__file__), "..", "data", "high_score.txt")
        with open(file_path, 'r') as r:
            self._high_score = int(r.read())

        if self._high_score < self._current_score:
            self._high_score = self._current_score
            with open(file_path, 'w') as w:
                w.write(str(self._current_score))
                
    def display(self):
        """Displays the live score."""
        self.clear()  # delete the old text
        self.color("white")
        self.goto(-265, 280)
        self.write(f"Score: {self._current_score}", align="center", font=("Arial", 10, "normal"))

    def increase_score(self):
        """Increases the score by 1."""
        self._current_score += 1

    def game_over_msg(self):
        """Shows the game over message, current score and high score."""
        self.clear()
        self._update_high_score()

        self.goto(0, 50)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("Arial", 30, "bold"))

        self.goto(0, -20)
        self.color("white")
        self.write(f"Score: {self._current_score}", align="center", font=("Arial", 20, "normal"))

        self.goto(0, -50)
        self.color("gold")
        self.write(f"Best: {self._high_score}", align="center", font=("Arial", 18, "bold"))

        self.goto(0, -140)
        self.color("lightgray")
        self.write("Press 'R' to restart\nPress 'Esc' to quit", align="center", font=("Arial", 12, "normal"))