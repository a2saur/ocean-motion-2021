'''
get the data
get the slice of the data
plot the slice
'''

# Import Libraries
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np
import datetime as dt

# Get Data
data_file = Dataset("/Users/brownscholar/Desktop/A2_Internship/data/atlantic-data.nc")
w_data = data_file.variables["w"]
latitude_data = data_file.variables["latitude"]
# time, lat, lon, depth

# Create Slice of Data for date
lat = 153# med = 76# max = 153

# Define variables
date_len = 1355
lat_len = 154
lon_len = 118

data_slice = w_data[:, lat, :, 0].reshape(date_len, lon_len)
data_slice_rotated = np.rot90(data_slice)

# Make Colormap
top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')

# Get time stamps
time_data = data_file.variables["time"]

year_list = []

start = dt.datetime(1950, 1, 1)

for i in range(0, len(time_data), 52):
	time_value = dt.timedelta(hours=int(time_data[i]))
	current_date = start+time_value
	year_list.append(current_date.year)


# Get Longitude Stamps
longitude_values = data_file.variables['longitude'][:]
for i in range(len(longitude_values)):
	longitude_values[i] = longitude_values[i] - 360


# Plot Data
skip = 52

fig, ax = plt.subplots()
ax.set_xticks(np.arange(0, len(time_data), skip))
ax.set_xticklabels(year_list, rotation=90, fontsize=7)
ax.set_yticks(np.arange(0, 118, 20))
ax.set_yticklabels(longitude_values[0::20], fontsize=7)

# Plot Data
plt.pcolormesh(data_slice_rotated, cmap=newcmp, vmax=1, vmin=-1)

plt.ylabel("Longitude")
plt.xlabel("Time")
plt.title("Hovmoller diagram at latitude = "+str(latitude_data[lat])+u'\N{DEGREE SIGN}'+" N")

plt.colorbar()
plt.savefig("/Users/brownscholar/Desktop/A2_Internship/hovmoller_plots/latitude_"+str(latitude_data[lat])+".png")
plt.show()