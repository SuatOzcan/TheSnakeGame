from turtle import Turtle, Screen
from random import Random

COLORS = ("red", "orange", "yellow", "green", "blue", "purple")
TURTLES = ("tim", "tom", "riza", "monariza", "hamit", "jennifer")

random = Random()

screen = Screen()
screen.setup(width = 500, height = 400)

player_guess = screen.textinput(title = "Make your bet!", prompt = "Which turtle is going to win the race? Enter a color: ")

y_position = - 100
turtle_objects = []

for i in range(6):
    turtle_objects.append(Turtle(shape = "turtle"))
    turtle_objects[i].speed(0)
    turtle_objects[i].color(COLORS[i])
    turtle_objects[i].penup()
    turtle_objects[i].goto((-230, y_position))
    y_position += 30


tim = Turtle()
tim.position()
tim.color()
tim.goto()
is_game_on = True 

for i in range(100):
    for j in range(len(turtle_objects)):
        turtle_objects[j].forward(random.randint(0,10))
        if turtle_objects[j].position()[0] >= 250:
            the_winner_color = turtle_objects[j].color()[0]
            print(f"The winner is {the_winner_color}.")
            is_game_on = False
            break
    if is_game_on == False:
        break

screen.exitonclick()