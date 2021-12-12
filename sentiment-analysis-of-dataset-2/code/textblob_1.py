from textblob import TextBlob

import pandas as pd
from ast import literal_eval
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
df = pd.read_csv('tweet-dataset-2-pnn.csv', encoding='ISO-8859-1')
y_real=[]
y_pred=[]

#df=df.head(int(len(df)*(20.0/100)))


for i in df.index:
    val=TextBlob(df['1'][i]).sentiment.polarity
    y_real.append(df['0'][i])

    if val>0:
        y_pred.append(1)
    elif val<0:
        y_pred.append(-1)
    else:
        y_pred.append(0)

print(y_real)
print(y_pred)

print(len(y_real))
print(accuracy_score(y_real,y_pred))
print(confusion_matrix(y_real,y_pred))
print(f1_score(y_real,y_pred,average='micro'))
