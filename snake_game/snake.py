from turtle import Turtle, Screen
import pygame
from food import *

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()
pygame.mixer.init()
collision_with_food_sound = pygame.mixer.Sound("collisionFood.mp3")
bite_tail = pygame.mixer.Sound("bite_tail.mp3")


class Snake:
    def __init__(self):
        self.snake_size = 3
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for _ in range(self.snake_size):
            new_turtle = Turtle("square")
            new_turtle.color("gray")
            self.turtles.append(new_turtle)
        for turtle in self.turtles:
            turtle.penup()
            turtle.goto(self.turtles.index(turtle) * (-20), 0)

    def move(self):
        """Move the snake"""
        # how to make the square follow the head?
        # The last square should take the position of the following and so-and-so until the first : the head
        for square_index in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[square_index - 1].xcor()
            new_y = self.turtles[square_index - 1].ycor()
            self.turtles[square_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        screen.onkeypress(self.go_up, "a")
        screen.onkeypress(self.go_down, "w")
        screen.onkeypress(self.go_left, "q")
        screen.onkeypress(self.go_right, "d")

    def get_longer(self, food_color):
        last_x = self.turtles[len(self.turtles) - 1].xcor()
        last_y = self.turtles[len(self.turtles) - 1].ycor()
        last_cor = (last_x, last_y)
        new_turtle = Turtle("square")
        new_turtle.color(food_color)
        new_turtle.penup()
        new_turtle.goto(last_cor)
        self.turtles.append(new_turtle)

    def collision_with_tail(self):
        for segment in self.turtles[1:]:
            # diff_angle = (segment.heading() - self.head.heading())
            if self.head.distance(segment) < 10:
                # sound
                bite_tail.play()
                # and diff_angle != 0):
                return True

    def collision_with(self, apple):
        """If the snake eat the food"""
        if self.head.distance(apple) < 15:
            collision_with_food_sound.play()
            return True

    def go_up(self):
        #IF THE SNAKE IS GOING UP IT'S NOT ALLOWED TO GO DOWN
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
