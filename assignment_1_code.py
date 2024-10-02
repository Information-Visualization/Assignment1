import matplotlib.pyplot as plt
import csv #used Python documentation to work this out
#import numpy as np


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

#used something similar in another class
def distance(city1, city2):
    