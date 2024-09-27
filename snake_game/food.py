import random
import time
import turtle
from turtle import Turtle
import random as r

COLORS = [
    "LightPink",  # Rose pastel clair
    "LightSalmon",  # Saumon clair
    "LightYellow",  # Jaune clair
    "LightGreen",  # Vert clair
    "LightBlue",  # Bleu clair
    "Lavender",  # Lavande
    "Pink",  # Rose
    "PeachPuff",  # Pêche clair
    "SkyBlue",  # Bleu ciel
    "Thistle",  # Chardon
    "Honeydew",  # Miel
    "MistyRose"  # Rose brumeux
]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food_color = r.choice(COLORS)
        self.shape("circle")
        self.penup()
        self.food_len = 0.5
        self.food_width = 0.5
        self.shapesize(self.food_len, self.food_width)
        self.color(self.food_color)
        self.x = r.randint(-280, 280)
        self.y = r.randint(-280, 280)
        self.goto(self.x, self.y)
        self.start_time = int(time.time() * 1000)
        self.current_time = 0
        self.duration = 1

    def refresh(self):
        if self.times_at():
            self.display_big_food()
            turtle.ontimer(self.hide_big_food, 2000)
            self.x = r.randint(-280, 280)
            self.y = r.randint(-280, 280)
            self.goto(self.x, self.y)
            self.start_time = self.current_time
        else:
            self.food_color = r.choice(COLORS)
            self.color(self.food_color)
            self.x = r.randint(-280, 280)
            self.y = r.randint(-280, 280)
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.goto(self.x, self.y)

    def display_big_food(self):
        self.food_len = 1
        self.food_width = 1
        self.shapesize(self.food_len, self.food_width)

    def hide_big_food(self):
        self.food_len = 0.5
        self.food_width = 0.5
        self.shapesize(self.food_len, self.food_width)
        self.x = r.randint(-280, 280)
        self.y = r.randint(-280, 280)
        self.goto(self.x, self.y)

    def times_at(self):
        self.duration = 15000
        self.current_time = int(time.time() * 1000)
        if self.current_time - self.start_time > self.duration:
            self.duration = r.randint(5000, 20000)
            return True
        return False
