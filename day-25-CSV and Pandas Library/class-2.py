import pandas

data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# #av = round(sum(temp_list)/len(temp_list))
# print(temp_list)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Data in Columns
# condition_list = (data["condition"])
# print(condition_list)

#Get Data from Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

def ctf(c):
    f = (c * 1.8) + 32
    return f

monday = data[data.day == "Monday"]
print(monday.condition)

print(ctf(monday.temp))

#Create a DataFrame from Scratch
data_dict = {
    "Characters": ["Odasto", "Lohse", "Rahimus", "Red Prince"],
    "Weapons": ["Two-Handed Sword", "Crossbow", "Daggers", "Wand"],
    "Class": ["Barbarian", "Ranger", "Scoundrel", "Wizard"]
}
data = pandas.DataFrame(data_dict)
data.to_csv("warriors_of_divinity2.csv")