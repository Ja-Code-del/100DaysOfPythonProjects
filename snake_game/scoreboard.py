from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
BIGFONT = ("Courrier", 96, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.score_view()
        self.hideturtle()

    def score_view(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_view()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=BIGFONT)
