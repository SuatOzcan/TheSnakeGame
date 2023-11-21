from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align = ALIGNMENT, font = FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)