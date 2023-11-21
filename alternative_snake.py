from turtle import Turtle

segments = []

class Snake:

        starting_positions = [(0,0),(-20,0),(-40,0)]
        

        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            segments.append(new_segment)
    
            def move(self):
                for segment in range(len(segments) - 1 , 0, -1):
                    new_x = segments[segment -1].xcor()
                    new_y = segments[segment -1].ycor()
                    segments[segment].goto(new_x, new_y)

                segments[0].forward(20)