from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align = ALIGNMENT, font = FONT)

    def add_point(self):
        self.score += 1
        self.update_score()