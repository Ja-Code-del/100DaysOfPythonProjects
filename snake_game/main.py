from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

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
    turtle.goto(turtles.index(turtle)*(-20), 0)

#TODO 2 - MOVE THE SNAKE

screen.exitonclick()
