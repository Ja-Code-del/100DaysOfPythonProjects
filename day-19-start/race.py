from turtle import Turtle, Screen
import random as r

tim = Turtle()
don = Turtle()
raph = Turtle()
mike = Turtle()
screen = Screen()
screen.setup(640, 480)

is_race_on = False
user_bet = screen.textinput("Make Your Bet", "Who will win? : ")


# state of Turtles function
def set_turtle_state(turtle_name, color, y_pos):
    turtle_name.shape("turtle")
    turtle_name.color(color)
    turtle_name.penup()
    turtle_name.goto(-310, y_pos)


def check_arrive(turtle_name):
    if turtle_name.xcor() > 300:
        return True


# state of Tim
set_turtle_state(tim, "green", 80)

# state of Don
set_turtle_state(don, "blue", 160)

# state of Raph
set_turtle_state(raph, "purple", -80)

# state of Mike
set_turtle_state(mike, "yellow", -160)
racers = {"don": don,
          "tim": tim,
          "raph": raph,
          "mike": mike}

checker = True
for key, value in racers.items():
    while value.xcor() < 300 and checker:
        for key1, value1 in racers.items():
            speed = r.randint(0, 10)
            value1.forward(speed)
            if check_arrive(value1):
                print(f"{key}'s arrived")
                checker = False

screen.exitonclick()
