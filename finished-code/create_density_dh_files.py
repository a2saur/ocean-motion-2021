from netCDF4 import Dataset
import numpy as np
import seawater as sw
import datetime as dt

# READ IN NETCDF FILE
data = Dataset("intern-data-t5.nc") # import data
dayIndex = 0 # what day we're looking at
time = data.variables["time"]

startDate = dt.datetime(1950,1,1,0,0,0)

for dayIndex in range(time.shape[0]):
    currentDate = startDate+dt.timedelta(hours=int(time[dayIndex]))
    day = currentDate.strftime("%y") + currentDate.strftime("%m") + currentDate.strftime("%d")

    # READ IN SALINITY, TEMPERATURE, DEPTH
    soData = data.variables["so"][dayIndex,:,:,:] # get so (Salinity) data
    toData = data.variables["to"][dayIndex,:,:,:] # get to (Temperature) data
    zoData = data.variables["zo"][dayIndex,:,:,:] # get zo (Geopotential Height) data
    depthData = data.variables["depth"][:] # get depth data

    file = open("/Users/brownscholar/Desktop/A2_Internship/data/density/density_"+str(day)+".gr", "w")
    file.write("") # clear file
    file.close()

    # HEADER
    file = open("/Users/brownscholar/Desktop/A2_Internship/data/density/density_"+str(day)+".gr", "a")
    file.write("1\n") # depth
    file.write("158\t122\n") # latitude, longitude

    # LOOP THROUGH SALINITY, TEMPERATURE, DEPTH AND CALCULATE THE DENSITY AT EACH GRID POINT USING sw.dens() FUNCTION
    for x in range(0,1):
      for y in range(0,158):
        for z in range(0,122):
        	# use sw.dens(salinity, temperature, pressure) and add to a file
        	density = sw.dens(soData[x, y, z], toData[x, y, z], depthData[0]) # get density at point (inputing salinity, temperature, and pressure)
        	# WRITE THE CALCULATED DENSITY TO FILE
        	file.write("\t")
        	file.write("%7f"%(1000-density))
        	file.write("\n")

    file.close()





startDate = dt.datetime(1950,1,1,0,0,0)

for dayIndex in range(time.shape[0]):
    currentDate = startDate+dt.timedelta(hours=int(time[dayIndex]))
    day = currentDate.strftime("%y") + currentDate.strftime("%m") + currentDate.strftime("%d")
    # -----GEOPOTENTIAL HEIGHT-----
    geoFile = open("/Users/brownscholar/Desktop/A2_Internship/data/dynamic-height/dynamic_height_"+str(day)+".gr", "w")
    geoFile.write("") # clear file
    geoFile.close()

    # HEADER
    geoFile = open("/Users/brownscholar/Desktop/A2_Internship/data/dynamic-height/dynamic_height_"+str(day)+".gr", "a")
    geoFile.write("1\n") # depth
    geoFile.write("158\t122\n") # atitude, longitude

    for x in range(0,1):
      for y in range(0,158):
        for z in range(0,122):
        	geoFile.write("\t")
        	geoFile.write("%7f"%(zoData[x, y, z]*100)) # str(round(float(zoData[x, y, z]*100), 5)))
        	geoFile.write("\n")

    geoFile.close()


