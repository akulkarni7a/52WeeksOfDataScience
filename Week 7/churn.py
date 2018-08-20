# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 09:28:28 2018

@author: akulkarni
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

plt.style.use('fivethirtyeight')

df = pd.read_csv("./Data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Data Exploration
sns.countplot(x="gender", data=df)
sns.countplot(x="gender",hue="Churn", data=df)

sns.countplot(x="SeniorCitizen",hue="Churn",data=df)

sns.countplot(x="Partner",hue="Churn",data=df)

sns.countplot(x="Dependents",hue="Churn",data=df)

df["ChurnDummy"] = df["Churn"].map({'No':0,'Yes':1})
sns.barplot(x="ChurnDummy",y="tenure",data=df)

sns.countplot(x="MultipleLines",hue="Churn",data=df)

sns.countplot(x="InternetService",hue="Churn",data=df)

sns.countplot(x="OnlineSecurity",hue="Churn",data=df)

sns.countplot(x="OnlineBackup",hue="Churn",data=df)

sns.countplot(x="DeviceProtection",hue="Churn",data=df)

sns.countplot(x="TechSupport",hue="Churn",data=df)

sns.countplot(x="StreamingTV",hue="Churn",data=df)

sns.countplot(x="StreamingMovies",hue="Churn",data=df)

sns.countplot(x="Contract",hue="Churn",data=df)

sns.countplot(x="PaperlessBilling",hue="Churn",data=df)

fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
sns.countplot(x="PaymentMethod",hue="Churn",data=df,ax=ax)

sns.barplot(x="ChurnDummy",y="MonthlyCharges",data=df)

sns.scatterplot(x="MonthlyCharges",y="TotalCharges",hue="Churn",data=df)
plt.scatter(x=df["MonthlyCharges"], y=df['TotalCharges'])

# Data Cleaning
df.info()
df.isnull().sum()
df.head()

# Data Prep
dfPartner = pd.get_dummies(df["Partner"])
dfPartner.columns = ["Partner - No","Partner - Yes"]
df = pd.concat([df,dfPartner],axis=1,join_axes=[df.index])
df = df.drop("Partner - No", axis=1)

dfDependents = pd.get_dummies(df["Dependents"])
dfDependents.columns = ["Dependents - No","Dependents - Yes"]
df = pd.concat([df,dfDependents],axis=1,join_axes=[df.index])
df = df.drop("Dependents - Yes", axis=1)

dfPhoneService = pd.get_dummies(df["PhoneService"])
dfPhoneService.columns = ["PhoneService - No","PhoneService - Yes"]
df = pd.concat([df,dfPhoneService],axis=1,join_axes=[df.index])
df = df.drop("PhoneService - Yes", axis=1)


dfMultipleLines = pd.get_dummies(df["MultipleLines"])
dfMultipleLines.columns = ['Multiple Lines - No','Multiple Lines - No Phone Service','Multiple Lines - Yes']
df = pd.concat([df,dfMultipleLines],axis=1,join_axes=[df.index])
df = df.drop("Multiple Lines - No", axis=1)

dfInternetService = pd.get_dummies(df["InternetService"])
dfInternetService.columns = ['InternetServce - DSL','InternetServce - Fiber Optic','InternetServce - No']
df = pd.concat([df,dfInternetService],axis=1,join_axes=[df.index])
df = df.drop('InternetServce - No', axis=1)

dfOnlineSecurity = pd.get_dummies(df["OnlineSecurity"])
dfOnlineSecurity.columns = ['OnlineSecurity - No','OnlineSecurity - No Internet Service','OnlineSecurity - Yes']
df = pd.concat([df,dfOnlineSecurity],axis=1,join_axes=[df.index])
df = df.drop('OnlineSecurity - No', axis=1)

dfOnlineBackup = pd.get_dummies(df["OnlineBackup"])
dfOnlineBackup.columns = ['OnlineBackup - No','OnlineBackup - No Internet Service','OnlineBackup - Yes']
df = pd.concat([df,dfOnlineBackup],axis=1,join_axes=[df.index])
df = df.drop('OnlineBackup - No', axis=1)

dfDeviceProtection = pd.get_dummies(df["DeviceProtection"])
dfDeviceProtection.columns = ['DeviceProtection - No','DeviceProtection - No Internet Service','DeviceProtection - Yes']
df = pd.concat([df,dfDeviceProtection],axis=1,join_axes=[df.index])
df = df.drop('DeviceProtection - No', axis=1)

dfTechSupport = pd.get_dummies(df["TechSupport"])
dfTechSupport.columns = ['TechSupport - No','TechSupport - No Internet Service','TechSupport - Yes']
df = pd.concat([df,dfTechSupport],axis=1,join_axes=[df.index])
df = df.drop('TechSupport - No', axis=1)

dfStreamingTV = pd.get_dummies(df["StreamingTV"])
dfStreamingTV.columns = ['StreamingTV - No','StreamingTV - No Internet Service','StreamingTV - Yes']
df = pd.concat([df,dfStreamingTV],axis=1,join_axes=[df.index])
df = df.drop('StreamingTV - No', axis=1)

dfStreamingMovies = pd.get_dummies(df["StreamingMovies"])
dfStreamingMovies.columns = ['StreamingMovies - No','StreamingMovies - No Internet Service','StreamingMovies - Yes']
df = pd.concat([df,dfStreamingMovies],axis=1,join_axes=[df.index])
df = df.drop('StreamingMovies - No', axis=1)

dfContract = pd.get_dummies(df["Contract"])
dfContract.columns = ['Contract - Month-to-Month','Contract - One year','Contract - Two year']
df = pd.concat([df,dfContract],axis=1,join_axes=[df.index])
df = df.drop('Contract - Month-to-Month', axis=1)

dfPaperlessBilling = pd.get_dummies(df["PaperlessBilling"])
dfPaperlessBilling.columns = ['PaperlessBilling - No','PaperlessBilling - Yes']
df = pd.concat([df,dfPaperlessBilling],axis=1,join_axes=[df.index])
df = df.drop('PaperlessBilling - No', axis=1)

dfPaymentMethod = pd.get_dummies(df["PaymentMethod"])
dfPaymentMethod.columns = ['Payment Method - Bank Transfer(automatic)','Payment Method - Credit Card(automatic)','Payment Method - Electronic Check(automatic)','Payment Method - Mailed Check(automatic)']
df = pd.concat([df,dfPaymentMethod],axis=1,join_axes=[df.index])
df = df.drop('Payment Method - Bank Transfer(automatic)', axis=1)

df.columns
df['TotalCharges'].fillna(0, inplace=True)
df['TotalCharges'][488] = 0
df['TotalCharges'][753] = 0
df['TotalCharges'][936] = 0
df['TotalCharges'][1082] = 0
df['TotalCharges'][1340] = 0
df['TotalCharges'][3331] = 0
df['TotalCharges'][3826] = 0
df['TotalCharges'][4380] = 0
df['TotalCharges'][5218] = 0
df['TotalCharges'][6670] = 0
df['TotalCharges'][6754] = 0

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], downcast="float")

# Machine Learning
X = df[['tenure','MonthlyCharges','TotalCharges','Partner - Yes', 'Dependents - No', 'PhoneService - No',
       'Multiple Lines - No Phone Service', 'Multiple Lines - Yes',
       'InternetServce - DSL', 'InternetServce - Fiber Optic',
       'OnlineSecurity - No Internet Service', 'OnlineSecurity - Yes',
       'OnlineBackup - No Internet Service', 'OnlineBackup - Yes',
       'DeviceProtection - No Internet Service', 'DeviceProtection - Yes',
       'TechSupport - No Internet Service', 'TechSupport - Yes',
       'StreamingTV - No Internet Service', 'StreamingTV - Yes',
       'StreamingMovies - No Internet Service', 'StreamingMovies - Yes',
       'Contract - One year', 'Contract - Two year', 'PaperlessBilling - Yes',
       'Payment Method - Credit Card(automatic)',
       'Payment Method - Electronic Check(automatic)',
       'Payment Method - Mailed Check(automatic)']]

y = df['Churn']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1)

sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

#logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

print('Accuracy of logistic regression classifier on test set:' + str(logreg.score(X_test, y_test)))

# Coefficients

logreg.coef_

features = ['tenure','MonthlyCharges','TotalCharges','Partner - Yes', 'Dependents - No', 'PhoneService - No',
       'Multiple Lines - No Phone Service', 'Multiple Lines - Yes',
       'InternetServce - DSL', 'InternetServce - Fiber Optic',
       'OnlineSecurity - No Internet Service', 'OnlineSecurity - Yes',
       'OnlineBackup - No Internet Service', 'OnlineBackup - Yes',
       'DeviceProtection - No Internet Service', 'DeviceProtection - Yes',
       'TechSupport - No Internet Service', 'TechSupport - Yes',
       'StreamingTV - No Internet Service', 'StreamingTV - Yes',
       'StreamingMovies - No Internet Service', 'StreamingMovies - Yes',
       'Contract - One year', 'Contract - Two year', 'PaperlessBilling - Yes',
       'Payment Method - Credit Card(automatic)',
       'Payment Method - Electronic Check(automatic)',
       'Payment Method - Mailed Check(automatic)']

coefficients = [-1.44288831, -0.40147985,  0.70799971,  0.02412424,  0.04651968,
         0.04221733,  0.04221733,  0.15037979, -0.23194105,  0.31444796,
        -0.11155581, -0.1431566 , -0.11155581, -0.05452412, -0.11155581,
        -0.00990597, -0.11155581, -0.13494921, -0.11155581,  0.13099126,
        -0.11155581,  0.18675245, -0.26849776, -0.60773245,  0.16194013,
        -0.01220328,  0.14313435, -0.01891716]


d = {'Features': features, 'Coefficients':coefficients}
coeff = pd.DataFrame(d, columns=['Features','Coefficients'])

# Probabilities
y_prob=logreg.predict_proba(X_test)

prob = pd.DataFrame(data=y_prob)
prob.columns = ['Not Churn','Churn']






