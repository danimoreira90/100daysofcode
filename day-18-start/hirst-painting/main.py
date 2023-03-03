# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirstpainting.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.penup()
tim.ht()
tim.setx(-250)
tim.sety(-250)
cy = 0
for jump in range(10):
    cy += 50
    tim.sety(-250 + cy)
    tim.setx(-250)
    for step in range(10):
        tim.dot(20, random.choice(color_list));
        tim.forward(50)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# directions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fast")
#
#
# for step in range(400):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))











screen = Screen()
screen.exitonclick()

