#####Questions#####
# 1. Gun Laws vs NRA Score
# 2. What days have the most gun incidents?/Month
# 3. Gun incidents vs population
# 3. Correlation to NFL/NBA Schedule?
# 4. Correlation vs Income/Home Value
# 5. Correlation with Age


import pandas as pd
import seaborn as sns
import datetime
from geopy.geocoders import Nominatim
from decimal import *
import time
import requests
geolocator = Nominatim()

df = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 5\Data\gun.csv")

congressCurrent = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 5\Data\legislators-current.csv")
congressOld = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 5\Data\legislators-historical.csv")
congressCurrent = congressCurrent.append(congressOld)

congressCurrent.columns
congressOld.columns

### Exploration ###
df["state"].value_counts()
df["date"].min()
df["date"].max()



##Question 2
datetime.datetime.today().weekday()
df["date"] = pd.to_datetime(df["date"],format="%Y-%m-%d")

def weekday(input,index):
    df.loc[index,"dayofweek"] = input.weekday()
        
for i in range(0,len(df.index)):
    weekday(df["date"][i],i)
    
df["state"].value_counts()
    
sns.factorplot(x="dayofweek", data=df, kind="count", palette="Paired", size=6, aspect=1.5)

def month(input,index):
    df.loc[index,"month"] = input.month
        
for i in range(0,len(df.index)):
    month(df["date"][i],i)
    
sns.factorplot(x="month", data=df, kind="count", palette="Paired", size=6, aspect=1.5)

#Why are gun incidents higher in January and March? Saturday and Sunday?

#Question 4
df["latitude"] = df["latitude"].astype("float32")
df["longitude"] = df["longitude"].astype("float32")
df["latitude"][0]
df["longitude"][0]



def zipcode(address,index):
    try:
        location = geolocator.reverse(address)
        df.loc[index,"zip"] = location.raw["address"]["postcode"]
    except "GeocoderTimedOut":
        return zipcode(address,index)
    
def latlng (x,index):
    URL = "https://maps.googleapis.com/maps/api/geocode/json"
    key = "AIzaSyCwRwNZ394xZVBOrrM29MsmwsD9Gkpo-70"
    PARAMS = {'latlng':x,"key":key}
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    df.loc[index,"zip"] = data["results"][0]["address_components"][6]["long_name"]
        
for i in range(65217,len(df.index)):
    time.sleep(0.5)
    try:
        address = str(df["latitude"][i]) + "," + str(df["longitude"][i])
        zipcode(address,i)
        #latlng(address,i)
    except:
        continue



        


address = str(df["latitude"][116]) + "," + str(df["longitude"][116])
print(address)
latlng(address)



#helpful code
df.head()
df.tail()
df.columns
df = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 6\Data\output.csv")
df.to_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 6\Data\output.csv")
