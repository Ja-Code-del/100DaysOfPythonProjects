from turtle import Turtle

ALIGNMENT = "center"
FONT = ("monospace", 24, "normal")
BIGFONT = ("courrier", 96, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=BIGFONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()
