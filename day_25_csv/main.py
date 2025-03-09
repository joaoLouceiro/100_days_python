import csv

import pandas
from pandas import Series, DataFrame

with open("weather_data.csv") as file:
    data = csv.reader(file)
    for r in data:
        print(r)

#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# d = data['temp'].to_list()
# print(sum(d) / len(d))
#
# print(Series.max(data['temp']))
#
# print(data[data.temp == data.temp.max()])

# TODO count squirrels by color

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_grouped_by_color=data.groupby(["Primary Fur Color"])
print(data_grouped_by_color)
data_count = data_grouped_by_color.count()["Unique Squirrel ID"]
print(data_count)
data_csv = data_count.to_csv()
print(data_csv)

with open('out.csv', "w") as file:
    file.write(data_csv)