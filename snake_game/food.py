from turtle import Turtle
import random as r


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.x = r.randint(-280, 280)
        self.y = r.randint(-280, 280)
        self.goto(self.x, self.y)

    def refresh(self):
        self.x = r.randint(-280, 280)
        self.y = r.randint(-280, 280)
        self.goto(self.x, self.y)
