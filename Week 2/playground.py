import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import pyplot
import mylib
from scipy.stats import kendalltau
df.head(2)

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentiment = analyzer.polarity_scores(df["tweets"][0])
print(sentiment["neg"])
#{'neg': 0.068, 'neu': 0.822, 'pos': 0.11, 'compound': 0.9999}

def sentimentAnalysis(string, index):
    sentiment = analyzer.polarity_scores(string)
    df.loc[index,"negative"] = sentiment["neg"]
    df.loc[index,"neutral"] = sentiment["neu"]
    df.loc[index,"positive"] = sentiment["pos"]
    df.loc[index,"compound"] = sentiment["compound"]

for item in range(0,len(df.index)):
    sentimentAnalysis(df["tweets"][item],item)
    
#graphs#
plt.subplots(figsize=(20,15))

#minutes played
sns.lmplot(x="MP",y="positive",data=df)
sns.lmplot(x="MP",y="negative",data=df)


#position
sns.violinplot(x="POSITION",y="positive", data=df)
sns.violinplot(x="POSITION",y="negative", data=df)

#points
sns.lmplot(x="POINTS",y="positive",data=df)
sns.lmplot(x="POINTS",y="negative",data=df)

#team##################################################
a4_dims = (10, 8)
fig, ax = pyplot.subplots(figsize=a4_dims)
boxplot = sns.boxplot(x="TEAM",y="positive", data=df, ax=ax)
boxplot.set_xticklabels(df["TEAM"], rotation=50)
plt.show()

a4_dims = (10, 8)
fig, ax = pyplot.subplots(figsize=a4_dims)
boxplot = sns.boxplot(x="TEAM",y="negative", data=df, ax=ax)
boxplot.set_xticklabels(df["TEAM"], rotation=50)
plt.show()

#######################################################

#GP
sns.lmplot(x="GP",y="positive",data=df)
sns.lmplot(x="GP",y="negative",data=df)

#salary
sns.lmplot(x="SALARY_MILLIONS",y="positive",data=df)
sns.lmplot(x="SALARY_MILLIONS",y="negative",data=df)

#age
a4_dims = (10, 8)
fig, ax = pyplot.subplots(figsize=a4_dims)
boxplot = sns.boxplot(x="AGE",y="positive", data=df, ax=ax)
plt.show()

a4_dims = (10, 8)
fig, ax = pyplot.subplots(figsize=a4_dims)
boxplot = sns.boxplot(x="AGE",y="negative", data=df, ax=ax)
plt.show()

#FG%
sns.lmplot(x="FG%",y="positive",data=df)
sns.lmplot(x="FG%",y="negative",data=df)

#3P%
sns.lmplot(x="3P%",y="positive",data=df)
sns.lmplot(x="3P%",y="negative",data=df)

#FT%
sns.lmplot(x="FT%",y="positive",data=df)
sns.lmplot(x="FT%",y="negative",data=df)

#AST
sns.lmplot(x="AST",y="positive",data=df)
sns.lmplot(x="AST",y="negative",data=df)

#W
sns.lmplot(x="W",y="positive",data=df)
sns.lmplot(x="W",y="negative",data=df)

#PAGEVIEWS
sns.lmplot(x="PAGEVIEWS",y="positive",data=df)
sns.lmplot(x="PAGEVIEWS",y="negative",data=df)

#Twitter Favorites
sns.lmplot(x="TWITTER_FAVORITE_COUNT",y="positive",data=df)
sns.lmplot(x="TWITTER_FAVORITE_COUNT",y="negative",data=df)


## Verb

#graphs#
plt.subplots(figsize=(20,15))

#minutes played
sns.lmplot(x="MP",y="positiveVerb",data=df)
sns.lmplot(x="MP",y="negativeVerb",data=df)


#position
sns.violinplot(x="POSITION",y="positiveVerb", data=df)
sns.violinplot(x="POSITION",y="negativeVerb", data=df)

#points
sns.lmplot(x="POINTS",y="positiveVerb",data=df)
sns.lmplot(x="POINTS",y="negativeVerb",data=df)

#team########################################################
a4_dims = (10, 8)
fig, ax = pyplot.subplots(figsize=a4_dims)
boxplot = sns.boxplot(x="TEAM",y="positiveVerb", data=df, ax=ax)
boxplot.set_xticklabels(df["TEAM"], rotation=50)
plt.show()

a4_dims = (10, 8)
fig, ax = pyplot.subplots(figsize=a4_dims)
boxplot = sns.boxplot(x="TEAM",y="negativeVerb", data=df, ax=ax)
boxplot.set_xticklabels(df["TEAM"], rotation=50)
plt.show()

#############################################################

#GP
sns.lmplot(x="GP",y="positiveVerb",data=df)
sns.lmplot(x="GP",y="negativeVerb",data=df)

#salary
sns.lmplot(x="SALARY_MILLIONS",y="positiveVerb",data=df)
sns.lmplot(x="SALARY_MILLIONS",y="negativeVerb",data=df)

#age
a4_dims = (10, 8)
fig, ax = pyplot.subplots(figsize=a4_dims)
boxplot = sns.boxplot(x="AGE",y="positiveVerb", data=df, ax=ax)
plt.show()

a4_dims = (10, 8)
fig, ax = pyplot.subplots(figsize=a4_dims)
boxplot = sns.boxplot(x="AGE",y="negativeVerb", data=df, ax=ax)
plt.show()

#FG%
sns.lmplot(x="FG%",y="positiveVerb",data=df)
sns.lmplot(x="FG%",y="negativeVerb",data=df)

#3P%
sns.lmplot(x="3P%",y="positiveVerb",data=df)
sns.lmplot(x="3P%",y="negativeVerb",data=df)

#FT%
sns.lmplot(x="FT%",y="positiveVerb",data=df)
sns.lmplot(x="FT%",y="negativeVerb",data=df)

#AST
sns.lmplot(x="AST",y="positiveVerb",data=df)
sns.lmplot(x="AST",y="negativeVerb",data=df)

#W
sns.lmplot(x="W",y="positiveVerb",data=df)
sns.lmplot(x="W",y="negativeVerb",data=df)

#PAGEVIEWS
sns.lmplot(x="PAGEVIEWS",y="positiveVerb",data=df)
sns.lmplot(x="PAGEVIEWS",y="negativeVerb",data=df)

#Twitter Favorites
sns.lmplot(x="TWITTER_FAVORITE_COUNT",y="positiveVerb",data=df)
sns.lmplot(x="TWITTER_FAVORITE_COUNT",y="negativeVerb",data=df)

df["TEAM"].value_counts()

