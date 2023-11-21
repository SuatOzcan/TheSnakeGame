from turtle import Turtle, Screen

tim_the_turtle =Turtle()
screen = Screen()
screen.listen()

def move_forwards():
    tim_the_turtle.forward(10)

def move_backwards():
    tim_the_turtle.backward(10)

def rotate_left():
    new_heading = tim_the_turtle.heading() + 10
    tim_the_turtle.setheading(new_heading)

def rotate_right():
    new_heading = tim_the_turtle.heading() - 10
    tim_the_turtle.setheading(new_heading)

def clear():
    tim_the_turtle.clear()
    tim_the_turtle.penup()
    tim_the_turtle.home()
    tim_the_turtle.pendown()

screen.onkey(rotate_right, "d")
screen.onkey(rotate_left, "a")
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(clear, "c")


screen.exitonclick()