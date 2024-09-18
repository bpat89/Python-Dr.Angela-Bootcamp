import turtle as t
import random

tim = t.Turtle()

colors = ["red", "orange red", "green yellow", "gold", "medium spring green", "blue", "amber"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
    # So we know that if we have 360 degrees divided by the number of sides, then we get the angle.
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range (3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
