import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import StandardScaler

df.columns
brand_dummies = pd.get_dummies(df["POSITION"])
df_final2 = pd.concat([df,brand_dummies], axis=1)
df_final2.head()
df_final2.columns

df_final2.isnull().sum()
df_final2.dropna(inplace=True)

scaler = StandardScaler()
feature_cols = ['AGE','FG%','3P%','2P%','eFG%','FT%', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'POINTS',
       'GP', 'MPG', 'SALARY_MILLIONS', 'PAGEVIEWS', 'TWITTER_FAVORITE_COUNT',
       'TWITTER_RETWEET_COUNT','C','PF', 'PG', 'SF', 'SG']

y = df_final2["negative"]
X = df_final2[feature_cols]
scaler.fit(X)
X_scaled = scaler.transform(X)


def train_test_rmse(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    linreg = LinearRegression()
    linreg.fit(X_train, y_train)
    y_pred = linreg.predict(X_test)
    return np.sqrt(metrics.mean_squared_error(y_test, y_pred))

train_test_rmse(X_scaled, y)