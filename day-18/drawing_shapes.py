import turtle
import random


def draw_shape(shape_sides):
    """ask a number of side that you want and this beauty draw it for you"""
    angle = int(360 / shape_sides)

    for _ in range(shape_sides):
        t.forward(50)
        t.right(angle)


t = turtle.Turtle()
turtle.colormode(255)
canva = turtle.Screen()
canva.setup(640, 380)
canva.bgcolor(33, 33, 33)

t.penup()
t.left(90)
t.forward(150)
t.right(90)
t.pendown()

sides = [3, 4, 5, 6, 8, 10, 12, 15, 18, 20]

for side in sides:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    t.pencolor(r, g, b)
    draw_shape(side)

turtle.exitonclick()
