import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

# Open vertical velocity file
w_file = './test/ss1a2ww.gr'
w = open(w_file, "r")

#open netcdf file
original_data = Dataset("/Users/brownscholar/Desktop/A2 Internship/n-atlantic-2018.nc")

#get latitude and longitude from netcdf file: 
lat = original_data.variables['latitude']
lon = original_data.variables['longitude']

num_lat = 158
num_lon = 122
levels = 1

# make empty numpy array of shape depth, lat, lon shape for storing w:
empty_arr = np.zeros((levels, num_lat, num_lon))

# use a loop to read w_file into the variable 
#(skip first two lines of the file)
w.readline()
w.readline()
for x in range(0,1):
	for y in range(0,158):
		for z in range(0,122):
			line = w.readline()
			empty_arr[x,y,z] = float(line)


#this stuff defines the colorspace
top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')




# plot the data:
plt.pcolormesh(empty_arr[0,2:-2,2:-2], cmap=newcmp)

# add the x and y ticks to your plot:
plt.xticks(np.arange(0,num_lon,10),lon[::10])
plt.yticks(np.arange(0,num_lat,10),lat[::10])


# add labels
# labels_to_add = {"Upwelling":"#F00", "Downwelling":"#00F"}
# for label in labels_to_add:
# 	plt.plot([],[], color=labels_to_add[label], label=label)


plt.colorbar()
plt.legend()
plt.show()