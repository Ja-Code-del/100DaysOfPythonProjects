from turtle import Turtle
import random as r

COLORS = [
    "LightPink",     # Rose pastel clair
    "LightSalmon",   # Saumon clair
    "LightYellow",   # Jaune clair
    "LightGreen",    # Vert clair
    "LightBlue",     # Bleu clair
    "Lavender",      # Lavande
    "Pink",          # Rose
    "PeachPuff",     # Pêche clair
    "SkyBlue",       # Bleu ciel
    "Thistle",       # Chardon
    "Honeydew",      # Miel
    "MistyRose"      # Rose brumeux
]



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food_color = r.choice(COLORS)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(self.food_color)
        self.x = r.randint(-280, 280)
        self.y = r.randint(-280, 280)
        self.goto(self.x, self.y)

    def refresh(self):
        self.food_color = r.choice(COLORS)
        self.color(self.food_color)
        self.x = r.randint(-280, 280)
        self.y = r.randint(-280, 280)
        self.goto(self.x, self.y)
