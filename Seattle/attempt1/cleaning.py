# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:28:36 2018

@author: AK
"""

import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfDataScience\Seattle\Data\seattle.csv", engine='python')
df.head()

#df = df[['Longitude','Latitude','Event Clearance Group','Event Clearance Date']]

df['Event Clearance Group'].value_counts()

crimeList = ['CAR PROWL','BURGLARY','SHOPLIFTING','AUTO THEFTS','NARCOTICS COMPLAINTS','ASSAULTS','MENTAL HEALTH','ARREST','ROBBERY','PROSTITUTION','HOMICIDE']

df = df[df['Event Clearance Group'].isin(crimeList)]

df = df.reset_index()

df['Event Clearance Date'] = pd.to_datetime(df['Event Clearance Date'],format='%m/%d/%Y %I:%M:%S %p')

df['Day of Week'] = df['Event Clearance Date'].dt.weekday_name
df['Month'] = df['Event Clearance Date'].dt.month
df['Hour'] = df['Event Clearance Date'].dt.hour
df['Year'] = df['Event Clearance Date'].dt.year

#df = df.groupby(['Zone/Beat','Event Clearance Group','Day of Week','Month']).count()
#df = df.reset_index()

step = 0.001
to_bin = lambda x: np.floor(x / step) * step
df["latbin"] = df.Latitude.map(to_bin)
df["lonbin"] = df.Longitude.map(to_bin)


dfGrouped = df.groupby(['latbin','lonbin','Event Clearance Group','Day of Week','Month']).count()
dfGrouped = dfGrouped.reset_index()
dfGrouped = dfGrouped[['latbin', 'lonbin', 'Event Clearance Group', 'Day of Week', 'Month','index']]
dfGrouped.columns = ['Latitude','Longitude','Event Clearance Group', 'Day of Week', 'Month','Frequency']






dfGrouped.drop('Unnamed: 0',axis=1,inplace=True)
dfGrouped = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfDataScience\Seattle\Data\GroupedOutput.csv")

dfGrouped.to_csv(r"C:\Users\AK\Desktop\52WeeksOfDataScience\Seattle\Data\GroupedOutput.csv", encoding="utf-8")
