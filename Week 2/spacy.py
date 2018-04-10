import spacy
nlp = spacy.load('en')
df.head()

def subjFunc(data, indexValue):
    doc = nlp(data)

    nounList = []
    verbList = []
    for token in doc:
        if token.pos_ == "PROPN":
            nounList.append(token.text)
        if token.pos_ == "VERB":
            verbList.append(token.text)

    
    nounString = nounList = ', '.join(nounList)
    verbString = verbList = ', '.join(verbList)
    
    df.set_value(indexValue,"noun",nounString) 
    df.set_value(indexValue,"verb",verbString) 

for row in range(0,len(df.index)):
    subjFunc(df["tweets"][row],row)
    
#noun
def sentimentAnalysis(string, index):
    sentiment = analyzer.polarity_scores(string)
    df.loc[index,"negativeNouns"] = sentiment["neg"]
    df.loc[index,"neutralNouns"] = sentiment["neu"]
    df.loc[index,"positiveNouns"] = sentiment["pos"]

for item in range(0,len(df.index)):
    sentimentAnalysis(df["noun"][item],item)
    
#Verb    
def sentimentAnalysis(string, index):
    sentiment = analyzer.polarity_scores(string)
    df.loc[index,"negativeVerb"] = sentiment["neg"]
    df.loc[index,"neutralVerb"] = sentiment["neu"]
    df.loc[index,"positiveVerb"] = sentiment["pos"]

for item in range(0,len(df.index)):
    sentimentAnalysis(df["verb"][item],item)
    