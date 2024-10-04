#import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd

#file_path = "./data/climate.csv"
#climate_info = DataFrame.to_dict(pd.read_csv(file_path))

#for city in climate_info:
#    if city
#        print(climate_info["lat"], climate_info["lon"])

#for cities in climate_info:
#    if climate_info.item("city") == "Chicago":
#        print(climate_info["lat"], climate_info["lon"])

#for city in climate_info:
#    if "city" == "Chicago":
#        print("lat", "lon")

#print(chicago_data[0])
#print(houston_data[0])
#print(miami_data[0])
#print(ny_data[0])
#print(sf_data[0])
#print(seattle_data[0])

#Distance between Chicago and Seattle is 2158.716642564714 miles
#Reader, no it was not

#plt.bar(dates, chicago_sunshine, color="red", alpha = 0.4)
#plt.bar(dates, houston_sunshine, color="orange", alpha = 0.4)
#plt.bar(dates, miami_sunshine, color="yellow", alpha = 0.4)
#plt.bar(dates, ny_sunshine, color="green", alpha = 0.4)
#plt.bar(dates, sf_sunshine, color="blue", alpha = 0.4)
#plt.bar(dates, seattle_sunshine, color="black", alpha = 0.4)
#plt.title("Sunshine by City")
#plt.xlabel("Month")
#plt.ylabel("Amount of Sunshine")
#plt.show()



plt.scatter(chicago_lon, chicago_total_sunshine, color="red")
plt.scatter(houston_lon, houston_total_sunshine, color="orange")
plt.scatter(miami_lon, miami_total_sunshine, color="yellow")
plt.scatter(ny_lon, ny_total_sunshine, color="green")
plt.scatter(sf_lon, sf_total_sunshine, color="blue")
plt.scatter(seattle_lon, seattle_total_sunshine, color="black")
plt.title("Does longitude affect yearly hours of sunshine?")
plt.xlabel("Longitude")
plt.ylabel("Amount of Sunshine")
plt.show()

plt.scatter(chicago_lon, chicago_lat, chicago_total_sunshine, color="red", alpha = 0.4)
plt.scatter(houston_lon, houston_lat, houston_total_sunshine, color="orange", alpha = 0.4)
plt.scatter(miami_lon, miami_lat, miami_total_sunshine, color="yellow", alpha = 0.4)
plt.scatter(ny_lon, ny_lat, ny_total_sunshine, color="green", alpha = 0.4)
plt.scatter(sf_lon, sf_lat, sf_total_sunshine, color="blue", alpha = 0.4)
plt.scatter(seattle_lon, seattle_lat, seattle_total_sunshine, color="black", alpha = 0.4)
plt.title("Do latitude and longitude affect yearly hours of sunshine?")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

plt.bar(chicago_lat, chicago_total_sunshine, color="red", alpha = 0.4)
plt.bar(houston_lat, houston_total_sunshine, color="orange", alpha = 0.4)
plt.bar(miami_lat, miami_total_sunshine, color="yellow", alpha = 0.4)
plt.bar(ny_lat, ny_total_sunshine, color="green", alpha = 0.4)
plt.bar(sf_lat, sf_total_sunshine, color="blue", alpha = 0.4)
plt.bar(seattle_lat, seattle_total_sunshine, color="black", alpha = 0.4)
plt.title("Does latitude affect yearly hours of sunshine?")
plt.xlabel("Latitude")
plt.ylabel("Total yearly hours of sunshine")
plt.show()

plt.scatter(chicago_lon, chicago_lat, chicago_total_sunshine, color="red", alpha = 0.4)
plt.scatter(houston_lon, houston_lat, houston_total_sunshine, color="orange", alpha = 0.4)
plt.scatter(miami_lon, miami_lat, miami_total_sunshine, color="yellow", alpha = 0.4)
plt.scatter(ny_lon, ny_lat, ny_total_sunshine, color="green", alpha = 0.4)
plt.scatter(sf_lon, sf_lat, sf_total_sunshine, color="blue", alpha = 0.4)
plt.scatter(seattle_lon, seattle_lat, seattle_total_sunshine, color="black", alpha = 0.4)
plt.title("Do latitude and longitude affect yearly hours of sunshine?")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

plt.bar(chicago_lon, chicago_lat, chicago_total_sunshine, color="red", alpha = 0.4)
plt.bar(houston_lon, houston_lat, houston_total_sunshine, color="orange", alpha = 0.4)
plt.bar(miami_lon, miami_lat, miami_total_sunshine, color="yellow", alpha = 0.4)
plt.bar(ny_lon, ny_lat, ny_total_sunshine, color="green", alpha = 0.4)
plt.bar(sf_lon, sf_lat, sf_total_sunshine, color="blue", alpha = 0.4)
plt.bar(seattle_lon, seattle_lat, seattle_total_sunshine, color="black", alpha = 0.4)
plt.title("Do latitude and longitude affect yearly hours of sunshine?")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

chicago_lat = float(chicago_data[0]["lat"])
chicago_lon = float(chicago_data[0]["lon"])

houston_lat = float(houston_data[0]["lat"])
houston_lon = float(houston_data[0]["lon"])

miami_lat = float(miami_data[0]["lat"])
miami_lon = float(miami_data[0]["lon"])

ny_lat = float(ny_data[0]["lat"])
ny_lon = float(ny_data[0]["lon"])

sf_lat = float(sf_data[0]["lat"])
sf_lon = float(sf_data[0]["lon"])

seattle_lat = float(seattle_data[0]["lat"])
seattle_lon = float(seattle_data[0]["lon"])

miami_min = min(miami_sunshine)
miami_max = max(miami_sunshine)

chicago_min = min(chicago_sunshine)
chicago_max = max(chicago_sunshine)

ny_min = min(ny_sunshine)
ny_max = max(ny_sunshine)

sf_min = min(sf_sunshine)
sf_max = max(sf_sunshine)

seattle_min = min(seattle_sunshine)
seattle_max = max(seattle_sunshine)

plt.scatter((chicago_max - chicago_min), chicago_lat, color="blue", alpha = 0.4)
plt.scatter((houston_max - houston_min), houston_lat, color="green", alpha = 0.4)
plt.scatter((miami_max - miami_min), miami_lat, color="red", alpha = 0.4)
plt.scatter((ny_max - ny_min), ny_lat, color="yellow", alpha = 0.4)
plt.scatter((sf_max - sf_min), sf_lat, color="black", alpha = 0.4)
plt.scatter((seattle_max - seattle_min), seattle_lat, color="orange", alpha = 0.4)