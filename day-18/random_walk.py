import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)
canva = turtle.Screen()
canva.setup(640, 380)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


movements = [True, False]
t.pensize(4)
t.speed(10)
t.shape("turtle")
for _ in range(1000):
    vert = random.choice(movements)
    horizon = random.choice(movements)

    if vert:
        t.color(random_color())
        t.forward(30)
        if horizon:
            t.right(90)
        else:
            t.left(90)
    else:
        t.backward(30)

turtle.exitonclick()
