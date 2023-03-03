# # import anothermodule
# # print(anothermodule.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOrchid1")
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokémon Name", ["Pikachu", "Charmander", "Squirtle", "Articuno"], "l")
table.add_column("Type", ["Electric", "Fire", "Water", "Flying/Ice"], "l")
print(table)

