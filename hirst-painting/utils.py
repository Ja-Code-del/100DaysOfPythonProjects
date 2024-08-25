import colorgram as c


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
