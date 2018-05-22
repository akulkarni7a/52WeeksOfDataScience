#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 09:01:38 2018

@author: anirudhkulkarni
"""
import pandas as pd
import seaborn as sns

df = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfDataScience\Seattle\Data\seattle.csv")
df.head()

df['Event Clearance Date'] = pd.to_datetime(df['Event Clearance Date'],format='%m/%d/%Y %H:%M:%S %p')
df['Event Clearance Date'] = pd.to_datetime(df['Event Clearance Date'],format='%Y-%m-%d %H:%M:%S')

#Date
df['year'] = pd.DatetimeIndex(df['Event Clearance Date']).year
df['month'] = pd.DatetimeIndex(df['Event Clearance Date']).month
df['dayofweek'] = pd.DatetimeIndex(df['Event Clearance Date']).dayofweek

sns.countplot(x="month", data=df[df['Event Clearance Group'] == 'CAR PROWL'])
sns.countplot(x="year", data=df[df['Event Clearance Group'] == 'CAR PROWL'])
sns.countplot(x="dayofweek", data=df[df['Event Clearance Group'] == 'CAR PROWL'])

#Weather
df['Event Clearance Date'].min()
df['Event Clearance Date'].max()


df['Event Clearance Group'].value_counts()

#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='TRAFFIC RELATED CALLS',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='SUSPICIOUS CIRCUMSTANCES',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='DISTURBANCES',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='LIQUOR VIOLATIONS',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='LIQUOR VIOLATIONS',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='TRESPASS',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='OTHER PROPERTY',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='FALSE ALARMS',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='ACCIDENT INVESTIGATION',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='MOTOR VEHICLE COLLISION INVESTIGATION',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='NUISANCE, MISCHIEF',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='PROPERTY DAMAGE',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='FALSE ALACAD',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='MENTAL HEALTH',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='HAZARDS',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='FRAUD CALLS',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='BEHAVIORAL HEALTH',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='NUISANCE, MISCHIEF',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='PERSON DOWN/INJURY',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='MISCELLANEOUS MISDEMEANORS ',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='BIKE',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='ANIMAL COMPLAINTS',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='LEWD CONDUCT',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='HARBOR CALLS',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='DRIVE BY (NO INJURY)',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='OTHER VICE',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='PUBLIC GATHERINGS',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='RECKLESS BURNING',value='Low Level')
#df['Event Clearance Group'] = df['Event Clearance Group'].replace(to_replace='VICE CALLS',value='Low Level')


#crime = pd.DataFrame(df['Event Clearance Group'].value_counts().reset_index())
#crime.columns = ['Event Clearance Group','Crime Counts']
#
#df = pd.merge(df,crime,on="Event Clearance Group",how="left")


######gmap1
gmap = gmplot.GoogleMapPlotter(47.611716, -122.343112, 13)
hidden_gem_lat, hidden_gem_lon = 47.611716, -122.343112
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')



carprowl = []
burglary = []
shoplifting = []
autothefts = []
narcotics = []
assaults = []
arrest = []
robbery = []
prostitution = []
homicide = []

for i in range(0,len(df.index)):
    if df['Event Clearance Group'][i] == "CAR PROWL":
        carprowl.append(tuple((df['Latitude'][i],df['Longitude'][i])))
    if df['Event Clearance Group'][i] == "BURGLARY":
        burglary.append(tuple((df['Latitude'][i],df['Longitude'][i])))
    if df['Event Clearance Group'][i] == "SHOPLIFTING":
        shoplifting.append(tuple((df['Latitude'][i],df['Longitude'][i])))
    if df['Event Clearance Group'][i] == "AUTO THEFTS":
        autothefts.append(tuple((df['Latitude'][i],df['Longitude'][i])))
    if df['Event Clearance Group'][i] == "NARCOTICS COMPLAINTS":
        narcotics.append(tuple((df['Latitude'][i],df['Longitude'][i])))
    if df['Event Clearance Group'][i] == "ASSAULTS":
        assaults.append(tuple((df['Latitude'][i],df['Longitude'][i])))
    if df['Event Clearance Group'][i] == "ARREST":
        arrest.append(tuple((df['Latitude'][i],df['Longitude'][i])))
    if df['Event Clearance Group'][i] == "ROBBERY":
        robbery.append(tuple((df['Latitude'][i],df['Longitude'][i])))
    if df['Event Clearance Group'][i] == "PROSTITUTION":
        prostitution.append(tuple((df['Latitude'][i],df['Longitude'][i])))
    if df['Event Clearance Group'][i] == "HOMICIDE":
        homicide.append(tuple((df['Latitude'][i],df['Longitude'][i])))
        
#maroon
carprowl_lats, carprowl_lons = zip(*carprowl)
gmap.scatter(carprowl_lats, carprowl_lons, '#87002a', size=10, marker=False)
             
#light blue             
burg_lats, burg_lons = zip(*burglary)
gmap.scatter(burg_lats, burg_lons, '#71abfc', size=10, marker=False)
 
#grey             
shop_lats, shop_lons = zip(*shoplifting)
gmap.scatter(shop_lats, shop_lons, '#39414c', size=10, marker=False)
    
#teal            
auto_lats, auto_lons = zip(*autothefts)
gmap.scatter(auto_lats, auto_lons, '#5bffce', size=10, marker=False)
      
#yellow             
nar_lats, nar_lons = zip(*narcotics)
gmap.scatter(nar_lats, nar_lons, '#ecff47', size=10, marker=False)
     
#orange             
ass_lats, ass_lons = zip(*assaults)
gmap.scatter(ass_lats, ass_lons, '#ff8956', size=10, marker=False)

#light purple             
arrest_lats, arrest_lons = zip(*arrest)
gmap.scatter(arrest_lats, arrest_lons, '#d6aaff', size=10, marker=False)

#light Green             
rob_lats, rob_lons = zip(*robbery)
gmap.scatter(rob_lats, rob_lons, '#97ff93', size=10, marker=False)
            
#purple             
pros_lats, pros_lons = zip(*prostitution)
gmap.scatter(pros_lats, pros_lons, '#a838ff', size=10, marker=False)
    
#red             
hom_lats, hom_lons = zip(*homicide)
gmap.scatter(hom_lats, hom_lons, '#ff3752', size=10, marker=False)


gmap.draw("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/my_map.html")


#####Mapbox
dfcar = df[df['Event Clearance Group'] == 'CAR PROWL']
dfcar = dfcar[['Longitude','Latitude']]
dfcar = dfcar.reset_index()
dfcar.drop(['index'],axis=1,inplace=True)
dfcar.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/Mapbox/carprowl.csv")

#burg
dfburg = df[df['Event Clearance Group'] == 'BURGLARY']
dfburg = dfburg[['Longitude','Latitude']]
dfburg = dfburg.reset_index()
dfburg.drop(['index'],axis=1,inplace=True)
dfburg.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/Mapbox/dfburg.csv")

#shoplifting
dfshop = df[df['Event Clearance Group'] == 'SHOPLIFTING']
dfshop = dfshop[['Longitude','Latitude']]
dfshop = dfshop.reset_index()
dfshop.drop(['index'],axis=1,inplace=True)
dfshop.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/Mapbox/dfshop.csv")

#AUTO THEFTS
dfauto = df[df['Event Clearance Group'] == 'AUTO THEFTS']
dfauto = dfauto[['Longitude','Latitude']]
dfauto = dfauto.reset_index()
dfauto.drop(['index'],axis=1,inplace=True)
dfauto.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/Mapbox/dfauto.csv")

#narcotics
dfnar = df[df['Event Clearance Group'] == 'NARCOTICS COMPLAINTS']
dfnar = dfnar[['Longitude','Latitude']]
dfnar = dfnar.reset_index()
dfnar.drop(['index'],axis=1,inplace=True)
dfnar.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/Mapbox/dfnar.csv")

#ASSAULTS
dfass = df[df['Event Clearance Group'] == 'ASSAULTS']
dfass = dfass[['Longitude','Latitude']]
dfass = dfass.reset_index()
dfass.drop(['index'],axis=1,inplace=True)
dfass.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/Mapbox/dfass.csv")

#ARREST
dfarrest = df[df['Event Clearance Group'] == 'ARREST']
dfarrest = dfarrest[['Longitude','Latitude']]
dfarrest = dfarrest.reset_index()
dfarrest.drop(['index'],axis=1,inplace=True)
dfarrest.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/Mapbox/dfarrest.csv")

#ROBBERY
dfrob = df[df['Event Clearance Group'] == 'ROBBERY']
dfrob = dfrob[['Longitude','Latitude']]
dfrob = dfrob.reset_index()
dfrob.drop(['index'],axis=1,inplace=True)
dfrob.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/Mapbox/dfrob.csv")

#Prostitution
dfpros = df[df['Event Clearance Group'] == 'PROSTITUTION']
dfpros = dfpros[['Longitude','Latitude']]
dfpros = dfpros.reset_index()
dfpros.drop(['index'],axis=1,inplace=True)
dfpros.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/Mapbox/dfpros.csv")

#HOMICIDE
dfhom = df[df['Event Clearance Group'] == 'HOMICIDE']
dfhom = dfhom[['Longitude','Latitude']]
dfhom = dfhom.reset_index()
dfhom.drop(['index'],axis=1,inplace=True)
dfhom.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/Mapbox/dfhom.csv")


####Helpful code
df.to_csv("/Users/anirudhkulkarni/Desktop/52WeeksOfDataScience/Week 7/Data/seattle.csv")
