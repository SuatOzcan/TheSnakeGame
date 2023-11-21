from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGNMENT = "left"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-50, 260)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", font = FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", alignment = ALIGNMENT, font = FONT)