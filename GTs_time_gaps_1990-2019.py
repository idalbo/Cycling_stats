#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing libraries and loading the files
import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.dates as mdates

# Load files
gaps_cycling = pd.read_csv("~/Gap_GTs_last30y.csv")

# Printing the file
gaps_cycling

# Transforming the times in the dataframe into usable times
time_giro = pd.to_datetime(gaps_cycling["Giro"])
time_tour = pd.to_datetime(gaps_cycling["Tour"])
time_vuelta = pd.to_datetime(gaps_cycling["Vuelta"])

# Removing empty cells
time_tour = time_tour[:-1]
time_vuelta = time_vuelta[:-1]

# Transforming the time into seconds
timeG_sec = time_giro.dt.minute*60+time_giro.dt.second
timeT_sec = time_tour.dt.minute*60+time_tour.dt.second
timeV_sec = time_vuelta.dt.minute*60+time_vuelta.dt.second

# Creating new vectors with the times, teh years, the GTs, and the riders finishing first-second, properly sorted
times = np.concatenate((timeG_sec,timeT_sec,timeV_sec),axis=0)
years = np.concatenate((gaps_cycling["Year"],gaps_cycling["Year"][:-1],gaps_cycling["Year"][:-1]),axis=0)
gts = ["Giro"]*30+["Tour"]*29+["Vuelta"]*29
riders = np.concatenate((gaps_cycling["Giro first-second"],gaps_cycling["Tour first-second"][:-1],gaps_cycling["Vuelta first-second"][:-1]),axis=0)
times = times/60 #back to minutes again

# Defining the data for the new structure
data ={'GT':gts,'Year':years,"Time":times,'Cyclists':riders}

# Creating the new structure with the properly sorted data and saving it as .csv
times_struc = pd.DataFrame(data)
times_struc.to_csv('Gap_times_GTs.csv',sep=',')

# Plotting the figure with the time gaps in the three GTs using seaborn, properly labeling the bars, and saving the figure 
plt.figure(figsize=(30,10))
ax = sns.barplot(x='Year',y='Time',hue='GT',data=times_struc,edgecolor=(0,0,0),
                  linewidth=2, palette=["pink","gold","red"])
plt.setp(ax.get_legend().get_texts(), fontsize='20') # for legend text
plt.setp(ax.get_legend().get_title(), fontsize='24') # for legend title
plt.yticks(np.arange(0,10,1))
plt.xlabel('Year',fontsize=20) 
plt.ylabel('Time [min]',fontsize=20) 
plt.title('Time gap between first and second in the GTs between 1990 and 2019',fontsize=24)
ax.tick_params(axis = 'both', which = 'major', labelsize = 18)

for i in range(0,30):
    if times[i]<5:
        ax.text(years[i]-1990-0.34,times[i]+len(riders[i])/10,riders[i], rotation =90)
    else:
        ax.text(years[i]-1990-0.34,times[i]-len(riders[i])/12,riders[i], rotation =90)
        
for i in range(30,59):
    if times[i]<5:
        ax.text(years[i]-1990-0.06,times[i]+len(riders[i])/10, riders[i], rotation =90)
    else:
        ax.text(years[i]-1990-0.06,times[i]-len(riders[i])/12,riders[i], rotation =90)
        
for i in range(59,len(times)):
    if times[i]<5:
        ax.text(years[i]-1990+0.22,times[i]+len(riders[i])/10,riders[i], rotation =90)
    else:
        ax.text(years[i]-1990+0.22,times[i]-len(riders[i])/12,riders[i], rotation =90)

        
plt.savefig('GC_differences_1st_2nd.png',dpi=500)

