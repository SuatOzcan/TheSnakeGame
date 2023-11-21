from turtle import Turtle

class Snake:
    def __init__(self):
        self.starting_positions = [(0,0),(-20,0),(-40,0)]
        self.segments = []
        self.move_distance = 20
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def expand(self):
        position = self.segments[-1].position()
        self.add_segment(position)

    def continuous_movement(self):
        for segment in range(len(self.segments) - 1 , 0, -1):
            new_x = self.segments[segment -1].xcor()
            new_y = self.segments[segment -1].ycor()
            self.segments[segment].goto(new_x, new_y)

        self.snake_head.forward(self.move_distance)
    
    def move_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def move_down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def move_left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def move_right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)