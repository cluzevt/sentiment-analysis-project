# Source of dataset: https://www.kaggle.com/kazanova/sentiment140

# I changed the names of the columns and deleted a few unnecessary columns in the code.

# Sentiment analysis of tweets using logistic regression and svc.
# In pre-processing of data we have used very naive approach :
# 1.Splitting the tweets in tokens using space as a delimiter.
# 2.Converting the words into lower case.
# 3.Ignoring the words containing characters other than alpha-numeric.
# 4.Using dictionary to map a token to count of sentiment (-1 is added if token belongs to tweet which has negative sentiment else +1 is added)
# 5.Finally sentiment for each tweet is mapped back to 0 and 1. Sum of the count of the value of each token is calculated and is mapped to 0 or 1 depending on the sentiment of the tweet.


# After that data is divided into 80-20 for training-testing purposes. Logistic regression and support vector machines have been used to predict sentiment of test data.


from sklearn.metrics import confusion_matrix
from sklearn import svm
import re
from sklearn.utils import shuffle
import pandas as pd
import nltk
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('../input/sentiment140/training.1600000.processed.noemoticon.csv', encoding='ISO-8859-1')

df.drop(df.loc[df['0'] == 2].index, inplace=True)

cols = [1, 2, 3, 4]
df.drop(df.columns[cols], axis=1, inplace=True)
df.rename(columns={df.columns[1]: '1'}, inplace=True)
df['0'].loc[(df['0'] > 0)] = 1
df['0'].loc[(df['0'] == 0)] = -1
df = shuffle(df)

# (df['0'] == 1).sum()
df = df.head(100000)
df['1'] = df.apply(lambda row: nltk.word_tokenize(row['1']), axis=1)
# df.head()

dict_count = {}

for i in range(0, len(df)):
    if i > 0.8 * len(df):
        continue
    list_val = []
    for val in df['1'].values[i]:
        val = val.lower()
        val = re.sub('\W+', '', val)
        if (len(val) > 0):
            list_val.append(val)
            if val in dict_count:
                dict_count[val] += df['0'].values[i]
            else:
                dict_count[val] = df['0'].values[i]
    df['1'].values[i] = list_val

# df.head()
df['0'].loc[(df['0'] == 1)] = 1
df['0'].loc[(df['0'] == -1)] = 0

x_val = []
y_val = []
x = []
y = []
for i in range(0, len(df)):
    temp = 0
    for val in df['1'].values[i]:
        if val in dict_count:
            temp += dict_count[val]

    if (i <= 0.8 * len(df)):
        x_val.append(temp)
        y_val.append(df['0'].values[i])
    else:
        x.append(temp)
        y.append(df['0'].values[i])

x_val = pd.DataFrame(x_val)
y_val = pd.DataFrame(y_val)
x = pd.DataFrame(x)
y = pd.DataFrame(y)

model = LogisticRegression()
model.fit(x_val, y_val)

Y = model.predict(x)

print("Confusion Matrix for LogisticRegression : ")
print(confusion_matrix(y, Y))
print("Accuracy : ")
print(accuracy_score(y, Y))

clf = svm.SVC()

clf.fit(x_val, y_val)

Y = clf.predict(x)

print("Confusion Matrix for SVM : ")
print(confusion_matrix(y, Y))
print("Accuracy : ")
print(accuracy_score(y, Y))

print("Total test data (around 20%) for both cases : ")
print(len(Y))
