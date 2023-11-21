from turtle import Screen, Turtle

screen = Screen()

screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("The Snake Game")

# x_position = 0

# turtle_objects = []

# for i in range(3):
#     turtle_objects.append(Turtle(shape = "square"))
#     turtle_objects[i].color("white")
#     turtle_objects[i].speed(0)
#     turtle_objects[i].penup()
#     turtle_objects[i].setpos((x_position, 0))

#     x_position -= 20

starting_positions = [(0,0),(-20,0),(-40,0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

screen.exitonclick()