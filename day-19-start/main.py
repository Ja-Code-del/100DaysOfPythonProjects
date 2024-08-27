from turtle import Turtle, Screen

tim = Turtle()
canva = Screen()

speed = 10


def move_forward():
    tim.setheading(90)
    tim.forward(speed)


def move_left():
    tim.setheading(180)
    tim.forward(speed)


def move_right():
    tim.setheading(0)
    tim.forward(speed)


def move_down():
    tim.setheading(270)
    tim.forward(speed)


def no_trace():
    tim.penup()


def trace():
    tim.pendown()


def reload():
    canva.resetscreen()


def draw_arc():
    tim.circle(50, 10)


canva.listen()
canva.onkeypress(move_forward, "w")
canva.onkeypress(move_down, "s")
canva.onkeypress(move_left, "a")
canva.onkeypress(move_right, "d")
canva.onkeypress(no_trace, "space")
canva.onkeyrelease(trace, "space")
canva.onkeyrelease(reload, "c")
canva.onkeyrelease(draw_arc, "v")

canva.exitonclick()
