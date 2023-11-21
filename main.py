from turtle import Screen
from snake import Snake
import time

screen = Screen()

screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    screen.onkey(snake.move_right, "d")
    screen.onkey(snake.move_left, "a")
    screen.onkey(snake.move_up, "w")
    screen.onkey(snake.move_down, "s")

screen.exitonclick()