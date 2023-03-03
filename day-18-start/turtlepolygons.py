from turtle import Turtle, Screen

def make_polygon(nsides, angle, color):

    for step in range(nsides):
        tim.right(angle)
        tim.forward(100)
    tim.color(color)

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
make_polygon(3,120, "DarkRed")
make_polygon(4,90, "DarkGray")
make_polygon(5,72, "cyan")
make_polygon(6,60, "DarkGoldenrod4")
make_polygon(7,(360/7), "DarkKhaki")
make_polygon(8,(360/8), "DarkBlue")
make_polygon(9,(360/9), "DarkSalmon")
make_polygon(10,(360/10), "DeepSkyBlue")













screen = Screen()
screen.exitonclick()