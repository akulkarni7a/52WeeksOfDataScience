import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import pyplot
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split
import spacy
nlp = spacy.load('en')
import gc
gc.collect()

#import data
df = pd.read_csv(r"C:\Users\AK\Dropbox\Data Science\Personal\52WeeksOfMachineLearning\Week 4\Data\articles1.csv", encoding='iso-8859-1')
df["publication"].value_counts()

df1 = pd.read_csv(r"C:\Users\AK\Dropbox\Data Science\Personal\52WeeksOfMachineLearning\Week 4\Data\articles2.csv", encoding='iso-8859-1')
df1["publication"].value_counts()

df2 = pd.read_csv(r"C:\Users\AK\Dropbox\Data Science\Personal\52WeeksOfMachineLearning\Week 4\Data\articles3.csv", encoding='iso-8859-1')
df2["publication"].value_counts()

#merging datasets
df = df.append(df1,ignore_index=True)
df = df.append(df2,ignore_index=True)

#cleaning
df["date"] = pd.to_datetime(df["date"],format="%Y-%m-%d")
df.info()

#visualizing Data
plt.figure(figsize=(25,3))
sns.countplot(x="publication", data=df)

df.date.min()
df.date.max()

plt.figure(figsize=(25,3))
sns.factorplot(x="month", data=df, kind="count", palette="Paired", size=6, aspect=1.5,hue="publication")

##SentimentAnalysis
analyzer = SentimentIntensityAnalyzer()
def sentimentAnalysisTitle(string, index):
    sentiment = analyzer.polarity_scores(string)
    df.loc[index,"TitleSentiment"] = sentiment["compound"]
    
def sentimentAnalysisContent(string, index):
    sentiment = analyzer.polarity_scores(string)
    df.loc[index,"ContentSentiment"] = sentiment["compound"]

for item in range(0,len(df.index)):
    try:
        sentimentAnalysisTitle(df["title"][item],item)
        sentimentAnalysisContent(df["content"][item],item)
    except:
        continue
    
##Graph Sentiment
titleSentimentDf = df.groupby("publication")["TitleSentiment"].mean()
contentSentimentDf = df.groupby("publication")["ContentSentiment"].mean()

sentimentDf = pd.concat([titleSentimentDf,contentSentimentDf],axis=1).reset_index()

sentimentDf.set_index('publication')

lm0 = sns.lmplot(x="TitleSentiment",y="ContentSentiment",hue="publication",data=sentimentDf,fit_reg=False,palette='Paired',size=6)
axes = lm0.axes
axes[0,0].set_ylim(-0.14,.4)
axes[0,0].set_xlim(-0.14,.4)
plt.plot(example.x, example.y)

##Stock Market
dowdf = pd.read_csv(r"C:\Users\AK\Dropbox\Data Science\Personal\52WeeksOfMachineLearning\Week 4\Data\DJI.csv")
spdf = pd.read_csv(r"C:\Users\AK\Dropbox\Data Science\Personal\52WeeksOfMachineLearning\Week 4\Data\GSPC.csv")
nasdaqdf = pd.read_csv(r"C:\Users\AK\Dropbox\Data Science\Personal\52WeeksOfMachineLearning\Week 4\Data\IXIC.csv")

dowdf.columns = ['date', 'Open', 'High', 'Low', 'Close', 'DowChange', 'Adj Close','Volume']
spdf.columns = ['date', 'Open', 'High', 'Low', 'Close', 'S&PChange', 'Adj Close','Volume']
nasdaqdf.columns = ['date', 'Open', 'High', 'Low', 'Close', 'NasdaqChange', 'Adj Close','Volume']

dowdf["date"] = pd.to_datetime(dowdf["date"],format="%m/%d/%Y")
spdf["date"] = pd.to_datetime(spdf["date"],format="%m/%d/%Y")
nasdaqdf["date"] = pd.to_datetime(nasdaqdf["date"],format="%m/%d/%Y")

dowdf = dowdf.drop(['Open', 'High', 'Low', 'Close', 'Adj Close','Volume'],axis=1)
spdf = spdf.drop(['Open', 'High', 'Low', 'Close', 'Adj Close','Volume'],axis=1)
nasdaqdf = nasdaqdf.drop(['Open', 'High', 'Low', 'Close', 'Adj Close','Volume'],axis=1)

df = pd.merge(df,dowdf,on="date", how="left")
df = pd.merge(df,spdf,on="date", how="left")
df = pd.merge(df,nasdaqdf,on="date", how="left")

df = df.dropna(subset=['DowChange'])

#######Machine Learning##############

###Logistic Regresion####

#Logistic Regression - Dow Change
df.isnull().sum()
df = df.dropna(subset=['TitleSentiment'])

X = df[['year','month', 'TitleSentiment', 'ContentSentiment']]
y = df['DowChange']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report
from sklearn import metrics

print(classification_report(y_test,predictions))
print (metrics.accuracy_score(y_test, predictions))
#52%

#Logistic Regression - S&P Change
X = df[['year','month', 'TitleSentiment', 'ContentSentiment']]
y = df['S&PChange']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report
from sklearn import metrics

print(classification_report(y_test,predictions))
print (metrics.accuracy_score(y_test, predictions))
#53%

#Logistic Regression - NasdaqChange Change
X = df[['TitleSentiment', 'ContentSentiment']]
y = df['NasdaqChange']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report
from sklearn import metrics

print(classification_report(y_test,predictions))
print (metrics.accuracy_score(y_test, predictions))
#58.75%


###Random Forest####
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=600)
rfc.fit(X_train,y_train)
predictions = rfc.predict(X_test)
print (metrics.accuracy_score(y_test, predictions))
#52.59%

###Sentiment Based on Presidents###
df = df.reset_index()

#content
for i in range(0,len(df.index)):
    if "Obama" in df["content"][i]:
        sentiment = analyzer.polarity_scores(df["content"][i])
        df.loc[i,"ObamaSentiment"] =  sentiment["compound"]
    if "Trump" in df["content"][i]:
        sentiment = analyzer.polarity_scores(df["content"][i])
        df.loc[i,"TrumpSentiment"] =  sentiment["compound"]


#title
for i in range(0,len(df.index)):
    if "Obama" in df["title"][i]:
        sentiment = analyzer.polarity_scores(df["title"][i])
        df.loc[i,"ObamaTitleSentiment"] =  sentiment["compound"]
    if "Trump" in df["title"][i]:
        sentiment = analyzer.polarity_scores(df["title"][i])
        df.loc[i,"TrumpTitleSentiment"] =  sentiment["compound"]
 
#sentiment of content with president in title
for i in range(0,len(df.index)):
    if "Obama" in df["title"][i]:
        sentiment = analyzer.polarity_scores(df["content"][i])
        df.loc[i,"ObamaTitleSentimentofContent"] =  sentiment["compound"]
    if "Trump" in df["title"][i]:
        sentiment = analyzer.polarity_scores(df["content"][i])
        df.loc[i,"TrumpTitleSentimentofContent"] =  sentiment["compound"]

#visualizing president sentiments
        
d = {'x': [-1, 1], 'y': [-1, 1]}
example = pd.DataFrame(data=d)
        
titleSentimentDfTrump = df.groupby("publication")["TrumpTitleSentiment"].mean()
titleSentimentDfObama = df.groupby("publication")["ObamaTitleSentiment"].mean()
sentimentDfPresidents = pd.concat([titleSentimentDfTrump,titleSentimentDfObama],axis=1).reset_index()

#title sentiment
lm = sns.lmplot(x="TrumpTitleSentiment",y="ObamaTitleSentiment",hue="publication",data=sentimentDfPresidents,fit_reg=False,palette='Paired',size=7)
axes = lm.axes
axes[0,0].set_ylim(-0.2,.06)
axes[0,0].set_xlim(-0.2,.06)
plt.plot(example.x, example.y)

#content sentiment where title = presidents
titleSentimentDfTrump = df.groupby("publication")["TrumpTitleSentimentofContent"].mean()
titleSentimentDfObama = df.groupby("publication")["ObamaTitleSentimentofContent"].mean()
sentimentDfPresidents = pd.concat([titleSentimentDfTrump,titleSentimentDfObama],axis=1).reset_index()

lm = sns.lmplot(x="TrumpTitleSentimentofContent",y="ObamaTitleSentimentofContent",hue="publication",data=sentimentDfPresidents,fit_reg=False,palette='Paired',size=7)
axes = lm.axes
axes[0,0].set_ylim(-0.2,1)
axes[0,0].set_xlim(-0.2,1)
plt.plot(example.x, example.y)



#helpful code
df.columns
df.head(10)
df.tail()
df[0]
df.to_csv(r"C:\Users\AK\Dropbox\Data Science\Personal\52WeeksOfMachineLearning\Week 4\Data\output.csv", encoding='iso-8859-1')
df = pd.read_csv(r"C:\Users\AK\Dropbox\Data Science\Personal\52WeeksOfMachineLearning\Week 4\Data\output.csv", encoding='iso-8859-1')
df = df.drop("Unnamed: 0",axis=1)
df = df.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1', 'Unnamed: 0.1.1.1'],axis=1)
df["date"] = pd.to_datetime(df["date"],format="%Y-%m-%d")
