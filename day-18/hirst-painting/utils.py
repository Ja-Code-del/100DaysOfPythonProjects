import colorgram as c
import random

def rgb_colors_extractor(image, numb_of_color):
    """extract rgb mode colors from an image.
    Using the package 'colorgram' imported as 'c'.
    So don't forget to install it before """

    colors_object = c.extract(image, numb_of_color)
    colors_tuple = []
    for i in range(len(colors_object)):
        colors_tuple.append(colors_object[i].rgb)

    rgb_colors = []
    for color in colors_tuple:
        r = color.r
        g = color.g
        b = color.b
        rgb_colors.append((r, g, b))


def hirst_dots_drawer(tom, colors, space_between_dots, numb_dot_per_line, numb_of_lines, dots_size):
    """Function to draw dots like Hirst painting : tom is your turtle name.
    colors is a list of rgb colors"""
    for _ in range(numb_of_lines):
        for _ in range(numb_dot_per_line):
            tom.pendown()
            tom.dot(dots_size, random.choice(colors))
            tom.penup()
            tom.forward(dots_size + space_between_dots)
        # print(tom.pos())
        tom.penup()
        tom.left(90)
        tom.forward(dots_size + space_between_dots)
        tom.right(90)
        tom.backward((dots_size * numb_dot_per_line) + (space_between_dots * numb_dot_per_line))
