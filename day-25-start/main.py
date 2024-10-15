import pandas

data = pandas.read_csv("weather_data.csv")
# extract the temperature column and turn it into a list with the 'to_list'
temp_list = data['temp'].to_list()
# print the average with the series method 'mean'
average_temp = data['temp'].mean()
# print(temp_list)
# average_temp = sum(temp_list) / len(temp_list)
print(f"Average Temperature : {average_temp}")
