import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv #used Python documentation to work this out
#import numpy as np

#function from DM-GY 9103 Machine Learning for Media workbook
def list_from_key(objects, key):
  new_list = []
  for city in objects:
    if key == "sunshine" or key == "lat" or key == "lon":
        new_list.append(float(city[key]))
    else:
        new_list.append(city[key])
  return new_list

file_path = "./data/climate.csv" 
climate_info = []
with open(file_path) as file:
    reader = csv.DictReader(file)
    for row in reader:
        climate_info.append(row)

chicago_data = []
houston_data = []
miami_data = []
ny_data = []
sf_data = []
seattle_data = []

for item in climate_info:
    if item["city"] == "Chicago":
        chicago_data.append(item)
    elif item["city"] == "Houston":
        houston_data.append(item)
    elif item["city"] == "Miami":
        miami_data.append(item)
    elif item["city"] == "New York":
        ny_data.append(item)
    elif item["city"] == "San Francisco":
        sf_data.append(item)
    elif item["city"] == "Seattle":
        seattle_data.append(item)

super_city_sunshine = list_from_key(climate_info, "sunshine")

chicago_sunshine = list_from_key(chicago_data, "sunshine")
houston_sunshine = list_from_key(houston_data, "sunshine")
miami_sunshine = list_from_key(miami_data, "sunshine")
ny_sunshine = list_from_key(ny_data, "sunshine")
sf_sunshine = list_from_key(sf_data, "sunshine")
seattle_sunshine = list_from_key(seattle_data, "sunshine")

monthlist = [i + 1 for i in range(12)]
dates = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

