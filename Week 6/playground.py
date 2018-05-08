#Questions:
#
#    1. Weather's impact on # of Passing, Running, Kicking Plays
#    2. Weather's impact on rushing yards, passing yards, kicking yards
#    3. Shotgun vs Under Center and Points Scored (Running vs Passing)
#    4. Icing the kicker
#    5. Passing Distance after throwing a pick (Do on full dataset)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
cf.go_offline()

print(__version__) # requires version >= 1.9.0

df = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 6\Data\nfl.csv")
weather = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 6\Data\weather.csv")

weather['date'] = pd.to_datetime(weather['date'])
weather = weather[weather['date']>'9/1/2009']

weather['home_team'].unique()
weather["home_team"] = weather["home_team"].map({'Pittsburgh Steelers':'PIT','Houston Texans':'HOU','New York Giants':'NYG',
       'Arizona Cardinals':'ARI','Seattle Seahawks':'SEA','Carolina Panthers':'CAR','Cleveland Browns':'CLE',
       'Atlanta Falcons':'ATL','Baltimore Ravens':'BAL','Green Bay Packers':'GB','Indianapolis Colts':'IND',
       'New Orleans Saints':'NO','Cincinnati Bengals':'CIN','Tampa Bay Buccaneers':'TB','Oakland Raiders':'OAK',
       'New England Patriots':'NE','Dallas Cowboys':'DAL','Chicago Bears':'CHI','Kansas City Chiefs':'KC',
       'Washington Redskins':'WAS','San Diego Chargers':'SD','San Francisco 49ers':'SF','Buffalo Bills':'BUF',
       'New York Jets':'NYJ','Philadelphia Eagles':'PHI','Denver Broncos':'DEN','Jacksonville Jaguars':'JAC',
       'Tennessee Titans':'TEN','Detroit Lions':'DET','Miami Dolphins':'MIA','Minnesota Vikings':'MIN','St. Louis Rams':'STL'})

weather['home_team'].value_counts()

weather.columns = ['id', 'HomeTeam', 'home_score', 'away_team', 'away_score',
       'temperature', 'wind_chill', 'humidity', 'wind_mph', 'weather', 'Date']

df['Date'] = pd.to_datetime(df['Date'])

newdf = pd.merge(df,weather,how="left",on=["Date",'HomeTeam'])

newdf = newdf[pd.notnull(newdf['temperature'])]

for i in range(0,len(newdf.index)):
    try:
        if newdf['temperature'][i] <= 32:
            newdf.loc[i,"temperatureCat"] = "Cold"
        if newdf['temperature'][i] > 32 and newdf['temperature'][i] <= 71:
            newdf.loc[i,"temperatureCat"] = "Pleasant"
        if newdf['temperature'][i] > 71:
            newdf.loc[i,"temperatureCat"] = "Hot"
    except:
        continue
    


####Grouped
groupedDF = newdf.groupby(['GameID','PlayType']).mean()
groupedDF = groupedDF.reset_index()

for i in range(0,len(groupedDF.index)):
    try:
        if groupedDF['temperature'][i] <= 32:
            groupedDF.loc[i,"temperatureCat"] = "Cold"
        if groupedDF['temperature'][i] > 32 and groupedDF['temperature'][i] <= 71:
            groupedDF.loc[i,"temperatureCat"] = "Pleasant"
        if groupedDF['temperature'][i] > 71:
            groupedDF.loc[i,"temperatureCat"] = "Hot"
    except:
        continue
    
###Temperature
temperatureDF = newdf.groupby('GameID').mean()
temperatureDF = temperatureDF[['temperature']]
temperatureDF = temperatureDF.reset_index()

#Pass
passDF = groupedDF[groupedDF['PlayType'] == 'Pass']

passyardsGraph = sns.factorplot(x="temperatureCat", y="Yards.Gained", data=passDF,
                   size=6, kind="bar", palette="muted")

passyardsGraph.set_ylabels("Pass Yards Gained")

passAttempts = newdf[newdf['PlayType'] == 'Pass'].groupby(['GameID']).count()
passAttempts = passAttempts[['Date']]
passAttempts.columns = ['Pass Attempts']
passAttempts = passAttempts.reset_index()

passDF = pd.merge(passDF,passAttempts, how="left",on="GameID")

passAttemptsGraph = sns.factorplot(x="temperatureCat", y="Pass Attempts", data=passDF,
                   size=6, kind="bar", palette="muted")

passAttemptsGraph.set_ylabels("Pass Attempts")

totalPassYardsDF = newdf.groupby(['GameID','PlayType']).sum()
totalPassYardsDF = totalPassYardsDF.reset_index()
totalPassYardsDF = totalPassYardsDF[totalPassYardsDF['PlayType'] == 'Pass']
totalPassYardsDF = pd.merge(totalPassYardsDF,temperatureDF,on='GameID',how='left')

sns.jointplot(x='temperature_y',y='Yards.Gained' , kind="hex", color="#4CB391", data=totalPassYardsDF)
sns.jointplot(x='temperature',y='Yards.Gained' , kind="hex", color="#4CB391", data=passDF)
sns.jointplot(x='temperature',y='Pass Attempts' , kind="hex", color="#4CB391", data=passDF)

#Run
sns.jointplot(x='temperature',y='Yards.Gained' , kind="hex", color="#4CB391", data=groupedDF[groupedDF['PlayType'] == 'Run'])

runDF = newdf.groupby(['GameID','PlayType']).sum()
runDF = runDF.reset_index()
runDF = runDF[runDF['PlayType'] == 'Run']
runDF = pd.merge(runDF,temperatureDF,on='GameID',how='left')
              
sns.jointplot(x='temperature_y',y='Yards.Gained' , kind="hex", color="#4CB391", data=runDF)
              
              
#Punting
puntdf = newdf.groupby(['GameID','PlayType']).sum()
puntdf = puntdf.reset_index()
puntdf = puntdf[puntdf['PlayType'] == 'Punt']
puntdf = pd.merge(puntdf,temperatureDF,on='GameID',how='left')
              
sns.jointplot(x='temperature_y',y='Yards.Gained' , kind="hex", color="#4CB391", data=puntdf)
       
#Field Goal
kickdf = newdf.groupby(['GameID','PlayType']).sum()
kickdf = kickdf.reset_index()
kickdf = kickdf[kickdf['PlayType'] == 'Field Goal']
kickdf = pd.merge(kickdf,temperatureDF,on='GameID',how='left')
              
sns.jointplot(x='temperature_y',y='FieldGoalDistance' , kind="hex", color="#4CB391", data=kickdf)


              
###Shotgun
for i in range(0,len(newdf.index)):
    try:
        if "Shotgun" in newdf['desc'][i]:
            newdf.loc[i,"Shotgun"] = 1
    except:
        continue

newdf['Shotgun'].fillna(0, inplace=True)

sns.factorplot(x="Shotgun", y="Yards.Gained", data=newdf,
                   size=6, kind="bar", palette="muted")  

sns.factorplot(x="Shotgun", y="AirYards", data=newdf,
                   size=6, kind="bar", palette="muted")    

sns.factorplot(x="temperatureCat", y="Yards.Gained",hue='Shotgun', data=newdf,
                   size=6, kind="bar", palette="muted")          
              

##Interception
for i in range(0,len(df.index)):
    try:
        if "INTERCEPT" in df['desc'][i]:
            df.loc[i,"Interception"] = 1
    except:
        continue



for i in range(0,len(df.index)):
    try:
        if df["Interception"][i] == 1:
            qb = df["Passer"][i]
            
            for j in range(i+1,len(df.index)):
                if df["Passer"][j] == qb:
                    print (df['Yards.Gained'][j])
                    df.loc[i,"Yards_after_Pick"] = df['Yards.Gained'][j]
                    break
    except:
        continue

df["Interception"].fillna(0,inplace=True)
    
yardsAfterPick = df.groupby(['Passer','Interception']).mean()
yardsAfterPick = yardsAfterPick.reset_index()
yardsAfterPick = yardsAfterPick[yardsAfterPick['Interception'] == 1]

passAttempts = df.groupby(['Passer']).count()
passAttempts = passAttempts[['Date']]
passAttempts.columns = ['Pass Attempts']
passAttempts = passAttempts.reset_index()

ints = df.groupby(['Passer']).sum()
ints = ints[['Interception']]
ints.columns = ['Career Interceptions']
ints = ints.reset_index()

yardsAfterPick = pd.merge(yardsAfterPick,passAttempts,how="left",on="Passer")
yardsAfterPick = pd.merge(yardsAfterPick,ints,how="left",on='Passer')
yardsAfterPick = yardsAfterPick[(yardsAfterPick['Pass Attempts']>100) & (yardsAfterPick['Career Interceptions']>10)]
yardsAfterPick = yardsAfterPick.sort_values('Yards_after_Pick', ascending=False)
              
g = sns.factorplot(x="Passer", y="Yards_after_Pick", data=yardsAfterPick,
                   size=6, kind="bar", palette="muted", aspect=9)
g.set_xticklabels(rotation=90)



yardsAfterPick.iplot(kind='bar',x='Passer',y='Yards_after_Pick')

####Helpful Code

newdf.tail()

df.head()
weather.head()
newdf.to_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 6\Data\output.csv")
