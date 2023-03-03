import turtle
from turtle import Turtle, Screen
import random



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["tim", "tom", "jon", "dan", "sam", "kim"]
all_turtles = []


def create_turtle(name, y, color):
    name = Turtle(shape="turtle")
    name.penup()
    name.goto(-230, y)
    name.color(color)


y = 0

for creation in range(0, 6):
    y += 40
    new_turtle = create_turtle(names[creation], (-150 + y), colors[creation])
    all_turtles.append(new_turtle)

while True:
    for turtle in all_turtles:
        turtle.forward(10)












screen.exitonclick()






