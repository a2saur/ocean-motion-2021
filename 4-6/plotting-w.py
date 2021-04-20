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

# Get Data
data_file = Dataset("/Users/brownscholar/Desktop/A2_Internship/data/atlantic-data.nc")
w_data = data_file.variables["w"]
# time, lat, lon, depth

# Create Slice of Data for date
date = 1190

# Define variables
date_len = 1355
lat_len = 154
lon_len = 118

data_slice = w_data[date, :, :, 0].reshape(lat_len, lon_len)

# Make Colormap
top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')

# Plot Data
plt.pcolormesh(data_slice, cmap=newcmp, vmin=-7, vmax=7)
plt.colorbar()
plt.show()