import pandas as pd
import pycmap
import matplotlib.pyplot as plt
import numpy as np

# Load in the data using pycmap with individual token
api = pycmap.API(token='5b820290-1db0-11ed-be7c-2b540ba2c4c4')       # call api using your unique API key
# Convert data read in to a pandas data frame
data_raw = api.get_dataset('tblHOT_Bottle')
# Look at the keys
data_raw.keys()

# Remove data with NaN in columns of interest
data = data_raw.dropna(subset=['NO2_NO3_bottle_hot'])
data = data.dropna(subset=['PO4_bottle_hot'])
data = data.dropna(subset=['SiO4_bottle_hot'])
data = data.dropna(subset=['temperature_ctd_bottle_hot'])
data = data.dropna(subset=['salinity_ctd_bottle_hot'])
data = data.dropna(subset=['oxygen_ctd_bottle_hot'])
data = data.dropna(subset=['chl_bottle_hot'])
# Filter for depth less than 300 m
data = data[data.depth<300]
# If we want to grid to every 20 m:
# data['binned_depth'] = data['depth']//20


# Make a profile plot for each nutrient with all the data overlaid
cols =['NO2_NO3_bottle_hot', 'PO4_bottle_hot', 'SiO4_bottle_hot']
fig, axs=plt.subplots(1,len(cols),figsize=(12, 4))
for j in np.arange(len(cols)):
    axs[j].scatter(data[cols[j]],data['pressure_ctd_bottle_hot'])
    axs[j].set_title(cols[j])
    axs[j].invert_yaxis()
    if j>0: 
        axs[j].set_yticklabels([])
axs[0].set_ylabel('Pressure [dbar]')
plt.show()

# Looks like we have about 2,383 measurements to work with
len(data)


