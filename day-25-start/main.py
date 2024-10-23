import pandas as pd

# Extract the data from the csv
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# colors = data["Primary Fur Color"]
# color_list = colors.to_list()
# gray_squirrel_count = cinnamon_squirrel_count = black_squirrel_count = 0

# for _ in color_list:
#     if _ == "Gray":
#         gray_squirrel_count += 1
#     elif _ == "Cinnamon":
#         cinnamon_squirrel_count += 1
#     elif _ == "Black":
#         black_squirrel_count += 1
#
# with open("squirrel_count.csv", 'w') as file: file.write(f"Color, Count\nGray, {gray_squirrel_count}\nCinnamon,
# {cinnamon_squirrel_count}\nBlack, {black_squirrel_count}")

# count the rows
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squir_count.csv")
