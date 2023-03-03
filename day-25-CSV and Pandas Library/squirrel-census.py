import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(black_squirrels_count)
# print(red_squirrels_count)
# print(grey_squirrels_count)

squirrel_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

squirrel_count = pandas.DataFrame(squirrel_dict)
squirrel_count.to_csv("squirrel_primary_color_count.csv")