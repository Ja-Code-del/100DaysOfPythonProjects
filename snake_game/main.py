from turtle import Screen
import time
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#CREATE SNAKE BODY
snake = Snake()
food = Food()

#MOVE THE SNAKE
#create the variable game_is_on
screen.listen()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
