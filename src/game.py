import os
import sys
import subprocess
import time
from turtle import Screen
from src.food import Food
from src.score import Score
from src.snake import Snake


STARTING_GAME_SPEED = 0.09
DELAY_DECELERATION_RATE = 0.00035
SNAKE_GROWTH = 3


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Snake")
screen.bgcolor("gray10")

snake = Snake()
score = Score()
food = Food()


def restart_game():
    """Restarts the entire python script."""
    path_to_run_py = os.path.join(os.path.dirname(__file__), "..", "run.py")
    subprocess.Popen([sys.executable, path_to_run_py])
    screen.bye()
    sys.exit()


def trigger_game_over():
    """Removes the live score, turtle and food. Then shows game over message."""
    food.hideturtle()
    for s in snake.snake_segments:
        s.hideturtle()
    score.game_over_msg()
    screen.onkeypress(restart_game, "R")
    screen.onkeypress(restart_game, "r")


def quit_game():
    screen.bye()


screen.listen()
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(quit_game, "Escape")


def run():
    food.respawn(snake.snake_segments)

    game_is_on = True
    while game_is_on:
        current_sleep = max(0.0001, STARTING_GAME_SPEED - (len(snake.snake_segments) * DELAY_DECELERATION_RATE))
        score.display()
        snake.move()

        if snake.head.distance(food) < 15:
            for _ in range(SNAKE_GROWTH):
                snake.new_segments()
            score.increase_score()
            food.respawn(snake.snake_segments)
        
        # tail collision
        for s in snake.snake_segments[1:]:
            if snake.head.distance(s) < 10:
                trigger_game_over()
                game_is_on = False

        # wall collision
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            trigger_game_over()
            game_is_on = False
        
        screen.update()
        time.sleep(current_sleep)