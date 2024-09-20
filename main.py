# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


# color_list = [(252, 252, 252), (238, 248, 243), (251, 242, 246), (226, 237, 246), (30, 106, 145), (229, 153, 80), (15, 169, 207), (148, 79, 30), (6, 57, 97), (31, 134, 77), (214, 133, 162), (138, 32, 51), (205, 156, 22), (118, 172, 194), (213, 93, 124), (235, 211, 85), (6, 103, 66), (145, 185, 167), (216, 209, 11), (3, 69, 136), (15, 49, 43), (76, 83, 23), (243, 168, 151), (134, 59, 83), (53, 60, 15), (223, 170, 191), (230, 100, 40), (1, 90, 120), (71, 157, 105), (164, 29, 25)]
import turtle
import random

# Define the color palette
# color_list = [
#     (231, 76, 60), (46, 204, 113), (52, 152, 219), (241, 196, 15),
#     (230, 126, 34), (155, 89, 182), (26, 188, 156), (192, 57, 43),
#     (39, 174, 96), (41, 128, 185), (243, 156, 18), (211, 84, 0),
#     (142, 68, 173), (22, 160, 133), (127, 140, 141), (236, 112, 99),
#     (82, 190, 128), (133, 193, 233), (244, 208, 63), (237, 187, 153),
#     (165, 105, 189), (72, 201, 176), (233, 150, 122), (231, 76, 60),
#     (241, 148, 138), (93, 173, 226), (245, 203, 167), (52, 73, 94),
#     (243, 104, 224), (245, 176, 65)
# ]
#
#
#
# # Set up turtle screen
# turtle.colormode(255)  # Set color mode to use RGB values
# tim = turtle.Turtle()
# tim.speed("fastest")
# tim.penup()  # We don't want lines between the dots
# tim.hideturtle()
#
# # Initial position
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
#
# # Draw a grid of 10x10 dots
# number_of_dots = 100
# dot_size = 20
# spacing = 50  # Spacing between dots
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(dot_size, random.choice(color_list))  # Draw dot with random color
#     tim.forward(spacing)
#
#     # Move up a row after every 10 dots
#     if dot_count % 10 == 0:
#         tim.setheading(90)  # Turn turtle to face upward
#         tim.forward(spacing)
#         tim.setheading(180)  # Move turtle left
#         tim.forward(spacing * 10)
#         tim.setheading(0)  # Face turtle right again
#
# # Exit on click
# turtle.Screen().exitonclick()


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [
    (231, 76, 60), (46, 204, 113), (52, 152, 219), (241, 196, 15),
    (230, 126, 34), (155, 89, 182), (26, 188, 156), (192, 57, 43),
    (39, 174, 96), (41, 128, 185), (243, 156, 18), (211, 84, 0),
    (142, 68, 173), (22, 160, 133), (127, 140, 141), (236, 112, 99),
    (82, 190, 128), (133, 193, 233), (244, 208, 63), (237, 187, 153),
    (165, 105, 189), (72, 201, 176), (233, 150, 122), (231, 76, 60),
    (241, 148, 138), (93, 173, 226), (245, 203, 167), (52, 73, 94),
    (243, 104, 224), (245, 176, 65)
]

tim.setheading(225)
tim.forward(350)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
