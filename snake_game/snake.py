from turtle import Turtle


class Snake:
    def __init__(self, snake_color):
        self.turtles = []
        for _ in range(3):
            new_turtle = Turtle("square")
            new_turtle.color(snake_color)
            self.turtles.append(new_turtle)
        for turtle in self.turtles:
            turtle.penup()
            turtle.goto(self.turtles.index(turtle) * (-20), 0)

    def move(self):
        for square_index in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[square_index - 1].xcor()
            new_y = self.turtles[square_index - 1].ycor()
            self.turtles[square_index].goto(new_x, new_y)

        self.turtles[0].forward(20)
        self.turtles[0].setheading(90)
