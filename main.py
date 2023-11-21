from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()

bait = Food()
bait.spawn_food()

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    if snake.snake_head.distance(bait) < 15:
        bait.spawn_food()
        scoreboard.add_point()

    screen.onkey(snake.move_right, "d")
    screen.onkey(snake.move_left, "a")
    screen.onkey(snake.move_up, "w")
    screen.onkey(snake.move_down, "s")

screen.exitonclick()