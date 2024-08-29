from turtle import Turtle, Screen

MOVE_DISTANCE = 20
screen = Screen()


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

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

        screen.onkeypress(self.go_up, "Up")
        screen.onkeypress(self.go_down, "Down")
        screen.onkeypress(self.go_left, "Left")
        screen.onkeypress(self.go_right, "Right")
        self.turtles[0].forward(MOVE_DISTANCE)

    def go_up(self):
        self.turtles[0].setheading(90)

    def go_down(self):
        self.turtles[0].setheading(270)

    def go_left(self):
        self.turtles[0].setheading(180)

    def go_right(self):
        self.turtles[0].setheading(0)
