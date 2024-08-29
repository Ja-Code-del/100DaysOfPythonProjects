from turtle import Screen
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#CREATE SNAKE BODY
snake = Snake("gray")

#MOVE THE SNAKE
#create the variable game_is_on
screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # how to make the square follow the head?
    # The last square should take the position of the following and so-and-so until the first : the head
    snake.move()


screen.exitonclick()
