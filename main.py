# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Pokemon Type"]
table.add_row(["Chespin", "Grass"])
# print(table.get_string(left_padding_width = 5))
table.add_rows([
    ["Braixen", "Fire"],
    ["Froakie", "Water"]
])
table.align = "l"
print(table)
