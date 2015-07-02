# First, you need to install the Basemap package  http://matplotlib.org/basemap/

from mpl_toolkits.basemap import Basemap

# Data of city location (logitude,latitude) and population

pop={'New York':8244910,'Los Angeles':3819702,
'Chicago':2707120,'Houston':2145146,
'Philadelphia':1536471,'Pheonix':1469471,
'San Antonio':1359758,'San Diego':1326179,
'Dallas':1223229,'San Jose':967487,
'Jacksonville':827908,'Indianapolis':827908,
'Austin':820611,'San Francisco':812826,
'Columbus':797434} # dictionary of the populations of each city

lat={'New York':40.6643,'Los Angeles':34.0194,
'Chicago':41.8376,'Houston':29.7805,
'Philadelphia':40.0094,'Pheonix':33.5722,
'San Antonio':29.4724,'San Diego':32.8153,
'Dallas':32.7942,'San Jose':37.2969,
'Jacksonville':30.3370,'Indianapolis':39.7767,
'Austin':30.3072,'San Francisco':37.7750,
'Columbus':39.9848} # dictionary of the latitudes of each city

lon={'New York':73.9385,'Los Angeles':118.4108,
'Chicago':87.6818,'Houston':95.3863,
'Philadelphia':75.1333,'Pheonix':112.0880,
'San Antonio':98.5251,'San Diego':117.1350,
'Dallas':96.7655,'San Jose':121.8193,
'Jacksonville':81.6613,'Indianapolis':86.1459,
'Austin':97.7560,'San Francisco':122.4183,
'Columbus':82.9850} # dictionary of the longitudes of each city


# build the map:
m = Basemap(llcrnrlon=-119,llcrnrlat=22, # define map corners
            urcrnrlon=-64, urcrnrlat=49,
            projection='lcc', # lambert conformal conic project
            lat_1=33,lat_2=45,lon_0=-95,resolution='c')

# draw the US:
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# draw the cities as translucent circles:
max_size=2000
for city in lon.keys():
    x, y = m(-lon[city],lat[city]) 
    m.scatter(x,y,max_size*pop[city]/pop['New York'],
              marker='o',color=niceblu, alpha=0.5)
plt.show()
