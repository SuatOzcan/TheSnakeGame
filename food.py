from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        # self.shape("circle")

    def spawn_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.dot(20, 'magenta')
        
        