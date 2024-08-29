from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#CREATE SNAKE BODY
#create an empty list of turtles
turtles = []
#for loop to create three square shape turtle
for _ in range(3):
    new_turtle = Turtle("square")
    new_turtle.color("white")
    turtles.append(new_turtle)

#set the position of the turtles to make them be closed each to other
#so that the result looks like a single object
#I am using their index to set their xcor.
for turtle in turtles:
    turtle.penup()
    turtle.goto(turtles.index(turtle)*(-20), 0)

#TODO 2 - MOVE THE SNAKE
#create the variable game_is_on
screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # how to make the square follow the head?
    # The last square should take the position of the following and so-and-so until the first : the head
    for square_index in range(len(turtles) - 1, 0, -1):
        new_x = turtles[square_index - 1].xcor()
        new_y = turtles[square_index - 1].ycor()
        turtles[square_index].goto(new_x, new_y)

    turtles[0].forward(20)
    turtles[0].setheading(90)


screen.exitonclick()
