#Questions:
#
#    1. Weather's impact on # of Passing, Running, Kicking Plays
#    2. Weather's impact on rushing yards, passing yards, kicking yards
#    3. Shotgun vs Under Center and Points Scored (Running vs Passing)
#    4. Passing Distance after throwing a pick (Do on full dataset)
#    5. Field Goals made by weather
#    6. Pass/Run/Field Goals Attempts by Team by Weather
#    7. # of Shotgun plays by weather

#importing packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#importing datasets
df = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 6\Data\nfl.csv")
weather = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 6\Data\weather.csv")

#cleaning weather dataset to prep for merge
weather['date'] = pd.to_datetime(weather['date'])
weather = weather[weather['date']>'9/1/2009']
weather["home_team"] = weather["home_team"].map({'Pittsburgh Steelers':'PIT','Houston Texans':'HOU','New York Giants':'NYG',
       'Arizona Cardinals':'ARI','Seattle Seahawks':'SEA','Carolina Panthers':'CAR','Cleveland Browns':'CLE',
       'Atlanta Falcons':'ATL','Baltimore Ravens':'BAL','Green Bay Packers':'GB','Indianapolis Colts':'IND',
       'New Orleans Saints':'NO','Cincinnati Bengals':'CIN','Tampa Bay Buccaneers':'TB','Oakland Raiders':'OAK',
       'New England Patriots':'NE','Dallas Cowboys':'DAL','Chicago Bears':'CHI','Kansas City Chiefs':'KC',
       'Washington Redskins':'WAS','San Diego Chargers':'SD','San Francisco 49ers':'SF','Buffalo Bills':'BUF',
       'New York Jets':'NYJ','Philadelphia Eagles':'PHI','Denver Broncos':'DEN','Jacksonville Jaguars':'JAC',
       'Tennessee Titans':'TEN','Detroit Lions':'DET','Miami Dolphins':'MIA','Minnesota Vikings':'MIN','St. Louis Rams':'STL'})
weather.columns = ['id', 'HomeTeam', 'home_score', 'away_team', 'away_score',
       'temperature', 'wind_chill', 'humidity', 'wind_mph', 'weather', 'Date']
df['Date'] = pd.to_datetime(df['Date'])

#merge two datasets together
newdf = pd.merge(df,weather,how="left",on=["Date",'HomeTeam'])

#remove null values in new dataset
newdf = newdf[pd.notnull(newdf['temperature'])]

#Assign Categorical Values for Temperature
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
    
#we'll need to reference temperature again in the future so let's create a temperature specific dataframe we can merge in the future
temperature = newdf.groupby(['GameID']).mean()
temperature.columns

#we're only interested in the temperature column so I'll only select that one
temperature = temperature[['temperature']]
#let's reassign the column name so we don't confuse it with temperature in future dataframes
temperature.columns = ['GameID','Temp']
temperature = temperature.reset_index()

##################Question 1: How does weather impact the number of running, passing, field goals called?##############################

#to help answer this question, we'll have to group this data by each game and the play type
countDF = newdf.groupby(['GameID','PlayType']).count()
    
#data cleaning
countDF = countDF.reset_index()

#let's add temperature back here so we can start graphing attempts vs weather
countDF = pd.merge(countDF,temperature,how="left",on="GameID")
countDF.columns
#this dataframe has a lot of columns - let's decrease memory usage by only selecting what we need
countDF = countDF[['GameID','PlayType','Date','Temp']]
countDF.columns = ['GameID', 'PlayType', 'Attempts', 'Temp']

#now, let's isolate each playtype. value counts lets us see the counts of each unique value in a column 
countDF['PlayType'].value_counts()

fieldGoalsAttemptedByTemp = countDF[countDF['PlayType']=='Field Goal']
PassAttemptedByTemp = countDF[countDF['PlayType']=='Pass']
RunsAttemptedByTemp = countDF[countDF['PlayType']=='Run']
SacksByTemp = countDF[countDF['PlayType']=='Sack']
PuntsByTemp = countDF[countDF['PlayType']=='Punt']

#let's start graphing
sns.violinplot(x="Temp", y="Attempts",data=fieldGoalsAttemptedByTemp, orient='h')
g = sns.lmplot(x="Temp", y="Attempts", size=5, data=PassAttemptedByTemp)
g.set_axis_labels("Temperature","Pass Attempts")

g = sns.lmplot(x="Temp", y="Attempts", size=5, data=RunsAttemptedByTemp)
g.set_axis_labels("Temperature","Rush Attempts")

sns.violinplot(x="Temp", y="Attempts",data=SacksByTemp, orient='h')

g = sns.lmplot(x="Temp", y="Attempts", size=5, data=PuntsByTemp)
g.set_axis_labels("Temperature","Punt Attempts")



######################Question 2: How does weather impact the yards gained by various play types?#############################

#let's look at the average yards gained by playtime in different weathers
meanDF = newdf.groupby(['GameID','PlayType']).mean()
meanDF = meanDF.reset_index()
meanDF = pd.merge(meanDF,temperature,how="left",on="GameID")
meanDF = meanDF[['GameID','PlayType','Yards.Gained','Temp']]

fieldGoalYardsByTemp = meanDF[meanDF['PlayType']=='Field Goal']
PassYardsByTemp = meanDF[meanDF['PlayType']=='Pass']
RunsYardsByTemp = meanDF[meanDF['PlayType']=='Run']
SackYardsByTemp = meanDF[meanDF['PlayType']=='Sack']
PuntYardsByTemp = meanDF[meanDF['PlayType']=='Punt']

#Graphing

#many games do not have field goals completed, so let's look at ones that have at least one field goal
g = sns.lmplot(x="Temp", y="Yards.Gained", size=5, data=fieldGoalYardsByTemp[fieldGoalYardsByTemp['Yards.Gained']>0])
g.set_axis_labels("Temperature","Field Goal Yards")

g = sns.lmplot(x="Temp", y="Yards.Gained", size=5, data=PassYardsByTemp)
g.set_axis_labels("Temperature","Pass Yards")

g = sns.lmplot(x="Temp", y="Yards.Gained", size=5, data=RunsYardsByTemp)
g.set_axis_labels("Temperature","Rush Yards")

g = sns.lmplot(x="Temp", y="Yards.Gained", size=5, data=SackYardsByTemp)
g.set_axis_labels("Temperature","Sack Yards")

g = sns.lmplot(x="Temp", y="Yards.Gained", size=5, data=PuntYardsByTemp)
g.set_axis_labels("Temperature","Punt Yards")


####################Question 3: How does playing in Shotgun effect the offense?#####################

for i in range(0,len(df.index)):
    try:
        if "Shotgun" in df['desc'][i]:
            df.loc[i,"Shotgun"] = 1
    except:
        continue

df['Shotgun'].fillna(0,inplace=True)
    
#pass yards vs rushing yards
for i in range(0,len(df.index)):
    try:
        if "Run" in df['PlayType'][i]:
            df.loc[i,"Run Yards"] = df['Yards.Gained'][i]
        if "Pass" in df['PlayType'][i]:
            df.loc[i,"Pass Yards"] = df['Yards.Gained'][i]
    except:
        continue


#To isolate when a play is in shotgun, we'll have to loop through the play description. because this doesn't include weather, let's go back to original df

sns.factorplot(x="Shotgun", y="Pass Yards", data=df,
                   size=6, kind="bar", palette="muted") 

sns.factorplot(x="Shotgun", y="Run Yards", data=df,
                   size=6, kind="bar", palette="muted") 

plt.figure(figsize=(20,12))
sns.countplot(x="PlayType_x", hue="Shotgun", data=df)

#shotgun & points scored
for i in range(0,len(df.index)):
    try:
        if "TOUCHDOWN" in df['desc'][i]:
            df.loc[i,"Touchdown"] = 1
    except:
        continue

df['Touchdown'].fillna(0,inplace=True)

sns.countplot(x="Shotgun", hue="Touchdown", data=df)


sns.factorplot(x="Shotgun", y="Touchdown", data=df,
                   size=6, kind="bar", palette="muted") 

##############################Question 4: QB's makeup after throwing a pick#############
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


############Machine Learning##################

###Cleaning######

df = df[df['PlayType'] == 'Pass']
df['Date'] = pd.to_datetime(df['Date'])
df['day_of_week'] = df['Date'].dt.weekday_name


for i in range(0,len(df.index)):
    try:            
        if "Shotgun" in df['desc'][i]:
            df.loc[i,"Shotgun"] = 1
    except:
        continue
    
df["Shotgun"].fillna(0,inplace=True)


##########Linear Regression##########

df = df[['down','yrdln','ydstogo','DefensiveTeam','Passer','QBHit','PassLocation','Yards.Gained','PassOutcome','Shotgun','day_of_week']]

defense_dummies = pd.get_dummies(df["DefensiveTeam"])
df = pd.concat([df,defense_dummies], axis=1)
df.drop(['DefensiveTeam'],axis=1,inplace=True)

location_dummies = pd.get_dummies(df["PassLocation"])
df = pd.concat([df,location_dummies], axis=1)
df.drop(['PassLocation'],axis=1,inplace=True)

day_dummies = pd.get_dummies(df["day_of_week"])
df = pd.concat([df,day_dummies], axis=1)
df.drop(['day_of_week'],axis=1,inplace=True)

df = df[df['PassOutcome'] == 'Complete']
df.drop(['PassOutcome'],axis=1,inplace=True)
df.drop(['Passer'],axis=1,inplace=True)
df = df[df['down'].notnull()]

df.isnull().sum()

y = df['Yards.Gained']
X = df.drop(['Yards.Gained'],axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
lm = LinearRegression()

lm.fit(X_train,y_train)
print('Coefficients: \n', lm.coef_)

predictions = lm.predict( X_test)

plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')

from sklearn import metrics
import numpy as np

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))


coeffecients = pd.DataFrame(lm.coef_,X.columns)
coeffecients.columns = ['Coeffecient']
coeffecients

from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

scores = np.sqrt(-cross_val_score(lm, X_scaled, y, cv=10, scoring='neg_mean_squared_error'))
print (scores.mean())

lm.fit(X_scaled,y)

df["Yards Pred"] = lm.predict(X_scaled)


##helpful code
df.to_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 6\Data\df.csv")
countDF.to_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 6\Data\countDF.csv")
newdf.to_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 6\Data\newdf.csv")
temperature.to_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 6\Data\temperature.csv")