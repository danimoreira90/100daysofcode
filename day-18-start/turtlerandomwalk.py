import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fast")


for step in range(400):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))











screen = Screen()
screen.exitonclick()