import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]

n = 0

tim.speed("fastest")
for step in range(80):
    n += 4.5
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(n)








screen = Screen()
screen.exitonclick()