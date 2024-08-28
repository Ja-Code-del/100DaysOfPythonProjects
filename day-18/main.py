from turtle import Turtle, Screen


def dashed_line():
    timmy.penup()
    timmy.right(180)
    timmy.forward(320)
    timmy.right(180)
    timmy.pendown()
    timmy.pensize(2)
    timmy.pencolor("white")
    for _ in range(15):
        timmy.forward(20)
        timmy.penup()
        timmy.forward(20)
        timmy.pendown()


def draw_straight_line():
    timmy.penup()
    timmy.left(90)
    timmy.forward(40)
    timmy.left(90)
    timmy.forward(640)
    timmy.right(180)
    timmy.pendown()
    timmy.pensize(20)
    timmy.forward(640)


def draw_other_straight_line():
    timmy.penup()
    timmy.right(90)
    timmy.forward(80)
    timmy.right(90)
    timmy.forward(640)
    timmy.right(180)
    timmy.pendown()
    timmy.pensize(20)
    timmy.forward(640)


screen = Screen()
screen.setup(width=640, height=380)
screen.bgcolor("gray")
timmy = Turtle()
timmy.shape("turtle")
timmy.color("black")

dashed_line()
draw_straight_line()
draw_other_straight_line()
screen.exitonclick()
