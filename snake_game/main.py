from turtle import Screen
import pygame
import time
from snake import Snake
from food import *
from scoreboard import ScoreBoard

session_one = True

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor(33, 33, 33)
screen.title("Snake Game")

pygame.mixer.init()
main_sound = pygame.mixer.Sound("main.mp3")
while session_one:

    main_sound.play(10000)
    screen.tracer(0)

    # CREATE SNAKE BODY
    snake = Snake()
    # CREATE THE FOOD
    food = Food()
    # CREATE THE SCOREBOARD
    scoreboard = ScoreBoard()

    # MOVE THE SNAKE
    # create the variable game_is_on
    screen.listen()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with the food
        if snake.collision_with(food):
            new_color = food.color()
            snake.get_longer(new_color[0])
            scoreboard.increase_score(food)
            food.refresh()

        # Detect collision with the wall
        if snake.head.xcor() > 290:
            snake.head.goto(-290, snake.head.ycor())

        if snake.head.xcor() < -290:
            snake.head.goto(300, snake.head.ycor())

        if snake.head.ycor() > 290:
            snake.head.goto(snake.head.xcor(), -290)

        if snake.head.ycor() < -290:
            snake.head.goto(snake.head.xcor(), 300)

        # Detect collision with the tail
        if snake.collision_with_tail():
            main_sound.stop()
            game_is_on = False
            session_one = False
    scoreboard.game_over()

screen.exitonclick()
