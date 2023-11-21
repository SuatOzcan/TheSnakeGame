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
screen.onkey(snake.move_right, "d")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")

bait = Food()
bait.spawn_food()

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)
    
    snake.continuous_movement()

    # Detect collision with the food.
    if snake.snake_head.distance(bait) < 15:
        bait.spawn_food()
        scoreboard.add_point()
        snake.expand()
    # Detect collision with the wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or \
    snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 15:
            game_is_on = False

scoreboard.game_over()

screen.exitonclick()