from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for _ in range(3):
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
        screen.onkeypress(self.go_up, "Up")
        screen.onkeypress(self.go_down, "Down")
        screen.onkeypress(self.go_left, "Left")
        screen.onkeypress(self.go_right, "Right")

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
