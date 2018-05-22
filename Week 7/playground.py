# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:02:35 2018

@author: AK
"""

import pandas as pd
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

df = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfDataScience\Week 7\Data\Traffic_Violations.csv")

df.head()

df = df[df['Latitude'].notnull()]
df = df.reset_index()

make = df['Make'].value_counts()
df = df.replace("TOYT","TOYOTA")
df = df.replace("HOND","HONDA")
df = df.replace("NISS","NISSAN")
df = df.replace("MERZ","Mercedes-Benz")
df = df.replace("MERCEDES","Mercedes-Benz")
df = df.replace("CHEVY","CHEVROLET")
df = df.replace("HYUN","HYUNDAI")
df = df.replace("ACUR","ACURA")
df = df.replace("VOLK","VOLKSWAGEN")
df = df.replace("DODG","DODGE")
df = df.replace("MITS","MITSUBISHI")
df = df.replace("CHRY","CHRYSLER")
df = df.replace("MAZD","MAZDA")
df = df.replace("CADI","CADILLAC")
df = df.replace("SUBA","SUBARU")
df = df.replace("VOLKSWAGON","VOLKSWAGEN")
df = df.replace("VW","VOLKSWAGEN")
df = df.replace("MERC","MERCURY")
df = df.replace("INFI","INFINITY")
df = df.replace("VOLKS","VOLKSWAGEN")
df = df.replace("PONT","PONTIAC")
df = df.replace("VOLV","VOLVO")
df = df.replace("TOYO","TOYOTA")
df = df.replace("LINC","LINCOLN")
df = df.replace("BUIC","BUICK")
df = df.replace("MERCEDEZ","Mercedes-Benz")
df = df.replace("OLDS","OLDSMOBILE")
df = df.replace("ISUZ","ISUZU")
df = df.replace("NISSIAN","NISSAN")
df = df.replace("MERCEDES BENZ","Mercedes-Benz")
df = df.replace("TOYOT","TOYOTA")
df = df.replace("TOYTA","TOYOTA")
df = df.replace("CHEVORLET","CHEVROLET")
df = df.replace("HYUND","HYUNDAI")
df = df.replace("PORS","PORSCHE")
df = df.replace("JAGU","JAGUAR")
df = df.replace("CHRYS","CHRYSLER")
df = df.replace("SCIO","SCION")
df = df.replace("SUZU","SUZUKI")
df = df.replace("SUZI","SUZUKI")
df = df.replace("PLYM","PLYMOUTH")
df = df.replace("CHRYSTLER","CHRYSLER")
df = df.replace("CADILAC","CADILLAC")
df = df.replace("HYUNDIA","HYUNDAI")
df = df.replace("CHEVEROLET","CHEVROLET")
df = df.replace("MITSU","MITSUBISHI")
df = df.replace("INFIN","INFINITY")
df = df.replace("SUBURU","SUBARU")
df = df.replace("TOYTOA","TOYOTA")
df = df.replace("MERCEDES-BENZ","Mercedes-Benz")
df = df.replace("MNNI","MINNI")
df = df.replace("CRYSLER","CHRYSLER")
df = df.replace("HUMM","HUMMER")
df = df.replace("MERZ BENZ","Mercedes-Benz")
df = df.replace("MAZADA","MAZDA")
df = df.replace("TOTY","TOYOTA")
df = df.replace("SUBU","SUBARU")
df = df.replace("CAD","CADILLAC")
df = df.replace("HYUNDA","HYUNDAI")
df = df.replace("HINDA","HONDA")
df = df.replace("JAG","JAGUAR")
df = df.replace("CHEVE","CHEVROLET")
df = df.replace("HYUNDAY","HYUNDAI")
df = df.replace("NISSA","NISSAN")
df = df.replace("TESL","TESLA")
df = df.replace("BENZ","Mercedes-Benz")
df = df.replace("HON","HONDA")
df = df.replace("NISAN","NISSAN")
make = df['Make'].value_counts()
make = make.reset_index()
vehicleList = make['index'].tolist()

vehicleList = []

df2 = df[df["Make"] == ]


def carScrapper(input):
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.autotrader.com/"+df['Make'][input]+"/"+df['Model'][input]+"/"+str(int(df['Year'][input])))
        el = driver.find_element_by_xpath('//*[@id="mountNode"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]')
        print(el.text)
        driver.close()
    except:
        driver.close()
        pass

for i in range(0,len(df.index)):
    if df['Make'][i] == 'HONDA':
        df.loc[i,"Car Value"] = carScrapper(i)
    if df['Make'][i] == "TOYOTA":
        df.loc[i,"Car Value"] = carScrapper(i)


df.to_csv(r"C:\Users\AK\Desktop\52WeeksOfDataScience\Week 7\Data\ouput.csv")
