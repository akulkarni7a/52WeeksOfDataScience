#Questions
#1. Which months have the most delays?
#2. Which airlines have the most delays?
#3. Which departing airports have the most delays?
#4. Which arriving airports have the most delays?
#5. Which day of the week have most delays
#6. Time of day with most delays?
#7. Delay correlated with distance?
#Hue - Cancelation Reason

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


train = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 5\train.csv")
test = pd.read_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 5\test.csv")

train.isnull().sum()

sns.countplot(x="Survived",data=train)

sns.countplot(x="Survived",hue="Sex", data=train)

sns.countplot(x="Survived",hue="Pclass", data=train)

sns.distplot(train["Age"].dropna(),kde=False,bins=30)

train['Fare'].hist(bins=40,figsize=(10,4))

sns.boxplot(x="Pclass",y='Age',data=train)

def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age
    
train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)

train.isnull().sum()

train.drop('Cabin',inplace=True,axis=1)
train.dropna(inplace=True)

train.isnull().sum()

sex = pd.get_dummies(train['Sex'],drop_first=True)
embark = pd.get_dummies(train['Embarked'],drop_first=True)

train = pd.concat([train,sex,embark],axis=1)

train.drop(['Sex','Embarked','Ticket'],axis=1,inplace=True)
train.drop(['Name','PassengerId'],axis=1,inplace=True)

plt.figure(figsize=(14,12))
sns.heatmap(train.astype(float).corr(),linewidths=0.1,vmax=1.0, 
            square=True, linecolor='white', annot=True)

train["Survived"] = train["Survived"].map({1:"Yes",0:"No"})

train.to_csv(r"C:\Users\AK\Desktop\52WeeksOfMachineLearning\Week 5\output.csv")


