import turtle as t
import random

tom = t.Turtle()
t.colormode(255)
canva = t.Screen()
canva.setup(640, 380)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


#angle = 0
#tom.pensize(2)
tom.speed("fastest")


def draw_spirograph(numb_circle):
    angle = round(360 / numb_circle)
    a = 0
    for _ in range(numb_circle):
        tom.color(random_color())
        tom.setheading(a)
        tom.circle(100)
        a += angle


draw_spirograph(100)

t.exitonclick()
