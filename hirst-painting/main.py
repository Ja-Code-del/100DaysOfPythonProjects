import turtle as t
import random

tom = t.Turtle()
t.colormode(255)
canva = t.Screen()
canva.setup(640, 380)

tom.penup()
tom.backward(300)
tom.right(90)
tom.forward(160)
tom.left(90)

x = 8
tom.speed("fastest")


colors = [(218, 173, 125), (159, 181, 190), (134, 73, 53), (50, 103, 154), (118, 81, 92), (179, 142, 152), (162, 104, 151), (42, 47, 66), (128, 174, 115), (83, 96, 183), (67, 9, 27), (82, 133, 107), (52, 63, 78), (228, 189, 141), (194, 91, 72), (220, 226, 221), (62, 49, 38), (115, 41, 56), (91, 143, 118), (70, 67, 52), (209, 181, 189), (181, 185, 210), (209, 183, 178), (89, 55, 47), (183, 201, 179), (172, 199, 204), (41, 73, 83)]

# METHODE WITHOUT DOT()
# for _ in range(50):
#     for _ in range(int(600 / (x + 2))):
#         tom.pensize(x)
#         tom.pendown()
#         tom.color(random.choice(colors))
#         tom.forward(1)
#         tom.penup()
#         tom.forward(x + 1)
#     tom.penup()
#     tom.left(90)
#     tom.forward(10)
#     tom.right(90)
#     tom.backward(600)

tom.pensize(x)
for _ in range(50):
    for _ in range(int(600 / (x + 2))):
        tom.pendown()
        tom.dot(8, random.choice(colors))
        tom.penup()
        tom.forward(x + 1)
    tom.penup()
    tom.left(90)
    tom.forward(10)
    tom.right(90)
    tom.backward(600)

t.exitonclick()
