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


canva.listen()
canva.onkeypress(move_forward, "Up")
canva.onkeypress(move_down, "Down")
canva.onkeypress(move_left, "Left")
canva.onkeypress(move_right, "Right")
canva.onkeypress(no_trace, "space")
canva.onkeyrelease(trace, "space")

canva.exitonclick()
