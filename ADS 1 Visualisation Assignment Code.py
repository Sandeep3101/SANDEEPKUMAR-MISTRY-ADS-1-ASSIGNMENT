# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 00:56:06 2022

@author: sanju
"""
# Import All The Python In-built Libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read The CSV File In To DataFrame And Print it
Electricity_Connections = pd.read_csv(r"C:\Users\sanju\.spyder-py3\Electricity Connections.csv")
print(Electricity_Connections)

# Sorting The first Five Row Of The DataFrame
Electricity_Connections_5 = Electricity_Connections.head()
print(Electricity_Connections_5)

# For Better Visualisation Set Fig configuration
plt.figure(figsize=(10,6), dpi=500)

''' Plotting The line plot of Electricity Connection Vs. Districts '''

plt.plot(Electricity_Connections_5["Districts"], Electricity_Connections_5["Industrial Connections"], label="Industrial Connections")
plt.plot(Electricity_Connections_5["Districts"], Electricity_Connections_5["Agriculture Connections"], label="Agriculture Connections")


# Setting x & y labels, Showing the legend and Title
plt.ylabel("CONNECTIONS")
plt.xlabel("NAME OF DISTRICTS")
plt.legend()
plt.title("ELECTRICITY CONNECTIONS OF DISTRICTS")

# Save the figure
plt.savefig("ELECTRICITY CONNECTIONS OF DISTRICTS.png")

plt.show()




''' Plotting The Bar Graph Comparing Two ELectricity Connections of Five Districts '''

# Seleting Districts Columns From DataFrame
Electricity_Connections_5_ = (Electricity_Connections_5["Districts"])

# Setting The Length Of Electricity Connections
X_axis = np.arange(len(Electricity_Connections_5_))

# Seleting Columns From DataFrame For Plotting
Other_Connections = (Electricity_Connections_5["Other Connections"])
Industrial_Connections = (Electricity_Connections_5["Industrial Connections"])

# For Better Visualisation Set Fig configuration
plt.figure(figsize=(10,6), dpi=500)

# Plotting Bar Graph of Selected Columns
plt.bar(X_axis - 0.2, Other_Connections, 0.4, label="Other Connections")
plt.bar(X_axis + 0.2, Industrial_Connections, 0.4, label="Commercial Connections")

# Setting x & y labels, Showing the legend, Title And X axis Ticks
plt.title("COMPARISON OF ELECTRICITY CONNECTIONS OF DISTRICTS")
plt.ylabel("CONNECTIONS")
plt.xlabel("NAME OF DISTRICTS")
plt.xticks(X_axis, Electricity_Connections_5_)
plt.legend()

# Save The figure
plt.savefig("COMPARISON OF ELECTRICITY CONNECTIONS OF DISTRICTS.png")

plt.show()




'''Plotting The Pie Chart To Show Electricity Connection Distribution With percentage'''

# Remove The 1st Column Of The DataFrame And Print it 
Electricity_Connections_5_ = Electricity_Connections_5.drop('Districts',axis=1)
print(Electricity_Connections_5_)

# Summation Of the Each Columns And Print it
Electricity_Connections_5_sum = Electricity_Connections_5_.sum(axis=0)
print(Electricity_Connections_5_sum)

# Remove The Industrial Connections Because of The Negligible Part of All-over Electricity Connections And Print it
Electricity_Connections_5_sum_ = Electricity_Connections_5_sum.drop('Industrial Connections',axis=0)
print(Electricity_Connections_5_sum_)

# Creat a List For Connection Label
connection = ['Domestic Connections','Agriculture Connections','Commercial Connections','Other Connections']

# For Good visualisation increase DPI 
plt.figure(dpi=500)

# Plotting The Data on Pie chart for Showing Sector Of Electricity Connection Distribution With percentage
plt.pie(Electricity_Connections_5_sum_, labels=connection,autopct='%1.1f%%')

# Set Title On Graph
plt.title("TYPES OF ELECTRICITY CONNECTION IN DISTRICTS")

# Save the figure
plt.savefig("TYPES OF ELECTRICITY CONNECTION.png")

plt.show()



