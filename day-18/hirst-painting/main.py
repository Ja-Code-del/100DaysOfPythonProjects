import turtle as t
import random
from utils import hirst_dots_drawer

tom = t.Turtle()
t.colormode(255)
canva = t.Screen()
canva.setup(680, 680)

# make tom starts at the lowest of the screen
tom.penup()
tom.backward(320)
tom.right(90)
tom.forward(300)
tom.left(90)

tom.speed("fastest")

colors = [(218, 173, 125), (159, 181, 190), (134, 73, 53), (50, 103, 154), (118, 81, 92), (179, 142, 152),
          (162, 104, 151), (42, 47, 66), (128, 174, 115), (83, 96, 183), (67, 9, 27), (82, 133, 107), (52, 63, 78),
          (228, 189, 141), (194, 91, 72), (220, 226, 221), (62, 49, 38), (115, 41, 56), (91, 143, 118), (70, 67, 52),
          (209, 181, 189), (181, 185, 210), (209, 183, 178), (89, 55, 47), (183, 201, 179), (172, 199, 204),
          (41, 73, 83)]

hirst_dots_drawer(tom, colors, 1, 300, 300, 5)

t.exitonclick()
