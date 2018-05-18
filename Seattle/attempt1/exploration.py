#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 09:01:38 2018

@author: anirudhkulkarni
"""
import pandas as pd
from gmplot import gmplot

df = pd.read_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/seattle.csv")
df.head()

gmap = gmplot.GoogleMapPlotter(47.611716, -122.343112, 13)

# Marker
hidden_gem_lat, hidden_gem_lon = 47.611716, -122.343112
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

df['Event Clearance Group'].value_counts()

#trafficArray = []
#SuspiciousCircum = []
#disturbances = []
#liquorViolations = []
carprowl = []

for i in range(0,len(df.index)):
    if df['Event Clearance Group'][i] == "CAR PROWL":
        carprowl.append(tuple((df['Latitude'][i],df['Longitude'][i])))
        
print(carprowl)

##Scatter
carprowl_lats, carprowl_lons = zip(*carprowl)
gmap.scatter(carprowl_lats, carprowl_lons, '#3B0B39', size=20, marker=False)


# Draw
gmap.draw("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/my_map.html")


##Cleaning for Mapbox
#car prowl
df['Event Clearance Group'].value_counts()

dfcar = df[df['Event Clearance Group'] == 'CAR PROWL']
dfcar = dfcar[['Longitude','Latitude']]
dfcar = dfcar.reset_index()
dfcar.drop(['index'],axis=1,inplace=True)
dfcar.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/carprowl.csv")

#BURGLARY
dfburg = df[df['Event Clearance Group'] == 'BURGLARY']
dfburg = dfburg[['Longitude','Latitude']]
dfburg = dfburg.reset_index()
dfburg.drop(['index'],axis=1,inplace=True)
dfburg.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/dfburg.csv")


