import pandas as pd
# import csv
#
# with open("weather_data.csv", "r") as wd:
#     # weather_data = wd.readlines()
#     weather_data = csv.reader(wd)
#     temperatures = []
#     for row in weather_data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

#
# df = pd.read_csv("weather_data.csv")


# print(df)
# print(df["temp"].mean())
# print(df["temp"].median())
# print(df["temp"].max())

# monday_temp = int(df[df.day == "Monday"]["temp"].iloc[0])
# monday_temp = int(df[df.day == "Monday"]["temp"][0])
# print(monday_temp * 1.8 + 32)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv", index=False)


# create squirrel_data.csv
# fur color - primary fur color
# count - count each squirrel with that color


df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(df[df["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(df[df["Primary Fur Color"] == "Black"])

df_out = pd.DataFrame(
    columns=["Fur Color", "Count"],
    data=[
        ["Gray", gray_squirrels_count],
        ["Cinnamon", cinnamon_squirrels_count],
        ["Black", black_squirrels_count],
    ]
)
print(df_out)
df_out.to_csv("squirrel_data.csv")