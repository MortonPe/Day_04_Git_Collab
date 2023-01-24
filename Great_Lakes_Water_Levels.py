<<<<<<< HEAD
=======
"""""
To use this notebook for your in-class assignment, you will need these 
files, which you shoujld have downloaded:
* mhu.csv -- Lake Michigan and Lake Huron
* sup.csv -- Lake Superior
* eri.csv -- Lake Erie
* ont.csv -- Lake Ontario

As instructed in the in-class activity notebook for today, you are 
only expected to complete one PART below. Do not worry if your group 
is not big enough to finish all parts below, but if you have extra 
time, you're welcome to do so.
"""""
>>>>>>> 62a9275649e686a282e8092fff2543084dec14f0
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# -

# PART 1
# Using the Michigan/Huron Dataset, plot the Water Level, the second 
# column, as a function of time years

data = pd.read_csv("mhu.csv")
plt.plot(data['time'],data['lake average'])

# PART 2
# Using the Superior Dataset, plot the Water Level, the second column, 
# as a function of time years



# PART 3
# Using the Erie Dataset, plot the Water Level, the second column, 
# as a function of time years

# +
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

erieData = pd.read_csv('eri.csv')
#erieData

xTime = erieData["time"]
yWaterLevel = erieData["water level"]

plt.plot(xTime, yWaterLevel)
plt.title("Lake Erie Water Levels Each Year")
plt.xlabel("Time")
plt.ylabel("Water Level")


# -

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

mhu

# PART 6
# Using the Michigan/Hurion and Erie Datasets, plot the 
# Michigan/Huron Water Level vs Erie Water Level to see if there is 
# any correlation between the water levels.

import pandas as pd
import matplotlib.pyplot as plt
mhu = pd.read_csv('mhu.csv')
eri = pd.read_csv('eri.csv')
mhu_level = mhu.iloc[0:,1]
eri_level = eri.iloc[0:,1]
plt.scatter(mhu_level, eri_level)


# PART 7
# Using the Superior and Ontario Datasets, plot the Superior Water 
# Level vs Ontario Water Level to see if there is any correlation 
# between the water levels.

sup = pd.read_csv('sup.csv')
ont = pd.read_csv('ont.csv')
#plt.plot(sup,ont)
x=sup['year']
y=sup['lake levels']
plt.plot(x,y)
c=ont['year']
v=ont['Lake Ontario annual averages']
plt.plot(c,v)


