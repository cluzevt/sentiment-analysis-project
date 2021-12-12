from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from ast import literal_eval
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
df = pd.read_csv('sentiment2.csv', encoding='ISO-8859-1')
y_real=[]
y_pred=[]

si=SentimentIntensityAnalyzer()
#df=df.head(int(len(df)*(20.0/100)))

for i in df.index:
    val1=si.polarity_scores(df['1'][i])
    val=val1['compound']
    y_real.append(df['0'][i])

    if val>= 0.05:
        y_pred.append(1)

    elif val<= - 0.05:
        y_pred.append(-1)
    else:
        y_pred.append(0)


print(y_real)
print(y_pred)

print(len(y_real))
print(accuracy_score(y_real,y_pred))
print(confusion_matrix(y_real,y_pred))
print(f1_score(y_real,y_pred,average='micro'))
