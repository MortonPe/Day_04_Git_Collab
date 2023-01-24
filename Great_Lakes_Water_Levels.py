import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# PART 1
# Using the Michigan/Huron Dataset, plot the Water Level, the second 
# column, as a function of time years



# PART 2
# Using the Superior Dataset, plot the Water Level, the second column, 
# as a function of time years



# PART 3
# Using the Erie Dataset, plot the Water Level, the second column, 
# as a function of time years



# PART 4
# Using the Ontario Dataset, plot the Water Level, the second column, 
# as a function of time years

ont_data = pd.read_csv("ont.csv")
time = ont_data['year']
averages = ont_data['Lake Ontario annual averages']
plt.plot(time,averages)
plt.xlabel('Time (years)')
plt.ylabel('Average water level')
plt.title('Average Lake Ontatiro Water Levels Over Time')
plt.tight_layout()

# PART 5
# Using the Michigan/Huron and Superior Datasets, plot the 
# Michigan/Hurion Water Level vs Superior Water Level to see if there 
# is any correlation between the water levels.



# PART 6
# Using the Michigan/Hurion and Erie Datasets, plot the 
# Michigan/Huron Water Level vs Erie Water Level to see if there is 
# any correlation between the water levels.



# PART 7
# Using the Superior and Ontario Datasets, plot the Superior Water 
# Level vs Ontario Water Level to see if there is any correlation 
# between the water levels.


